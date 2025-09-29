"""Implements a knowledge base conversation flow using Azure AI Search and local ChromaDB.

This module provides a production-ready KB agent implementation (ConversationFlow)
featuring deterministic "direct" mode and LLM-composed "assist" mode.
It handles policy-aware backend selection (Azure vs. Local), robust preflight
validation for Azure dependencies, safe fallbacks, and secure configuration handling.
The main entry points are `get_conversation_response` (non-streaming) and
`get_streaming_conversation_response` (streaming). It relies on external
Azure services and local file storage for ChromaDB persistence.
"""

# -----------------------------------------------------------------------------
# Knowledge Base Conversation Flow (Azure AI Search + local ChromaDB)
#
# This module implements a production-ready KB agent with:
# - Deterministic "direct" mode and optional "assist" mode (LLM composed).
# - Policy-aware backend selection (azure_only / prefer_azure / prefer_local / local_only).
# - Robust preflight validation for Azure (sync config checks + async network check).
# - Safe fallbacks, strict secret masking, and minimal, explicit user-facing messages.
# - Thoughtful handling of top_k resolution (request > env > defaults) and mode coercion.
#
# The code is heavily commented from top to bottom to explain every important decision.
# -----------------------------------------------------------------------------

from __future__ import annotations

import asyncio
import json
import logging
import os
import time
import uuid
from types import SimpleNamespace
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncIterator,
    Awaitable,
    Dict,
    List,
    Optional,
    Protocol,
    Tuple,
    cast,
)

# Re-exported for test monkey-patching compatibility
from autogen_agentchat.agents import AssistantAgent as _AssistantAgent
from autogen_core import (  # noqa: F401 (CancellationToken kept for API parity)
    EVENT_LOGGER_NAME,
    CancellationToken,
)
from autogen_core.tools import FunctionTool as _FunctionTool
from pydantic import SecretStr

from ingenious.client.azure import AzureClientFactory
from ingenious.models.chat import ChatRequest, ChatResponse, ChatResponseChunk
from ingenious.services.azure_search.client_init import make_async_search_client
from ingenious.services.chat_services.multi_agent.service import IConversationFlow
from ingenious.services.retrieval.errors import PreflightError


class _SearchConfigLike(Protocol):
    search_index_name: str
    search_endpoint: str
    search_key: SecretStr


# Back-compat names so tests can patch: knowledge_base_agent.FunctionTool / AssistantAgent
FunctionTool = _FunctionTool
AssistantAgent = _AssistantAgent

__all__ = ["ConversationFlow", "FunctionTool", "AssistantAgent"]

if TYPE_CHECKING:
    # Imports for ConversationFlow attributes (assuming Service inheritance)
    # Imports used in methods

    from ingenious.config.config import Config

    # Imports used dynamically or optionally
    from ingenious.services.chat_services.service import ChatService


# Safe, conservative defaults for k-values in each mode.
_TOPK_DIRECT_DEFAULT: int = 3
_TOPK_ASSIST_DEFAULT: int = 5

# Try YAML; fall back to JSON/plaintext if PyYAML isn't installed
try:
    import yaml  # type: ignore[import-untyped]
except Exception:
    yaml = None  # sentinel to denote "no YAML available"


class ConversationFlow(IConversationFlow):
    """
    Knowledge base conversation flow.

    - Non-streaming: direct KB search by default (deterministic "direct" mode).
       Optional "assist" mode uses AssistantAgent.on_messages for LLM summarization.
    - Streaming: uses AssistantAgent.run_stream and forwards content; robust error chunking,
       final flush to surface terminal results, and safe token-count fallback.
    - Careful resource/handler lifecycle with policy-controlled Azure/Chroma selection.
    """

    if TYPE_CHECKING:
        # Attributes initialized by IConversationFlow/Service parent class
        _config: Config
        _chat_service: ChatService | None
        # Attributes used internally
        _last_mem_warn_ts: float
        _kb_path: str
        _chroma_path: str

    def __init__(
        self,
        *args: Any,
        knowledge_base_path: Optional[str] = None,
        chroma_persist_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Construct a ConversationFlow.

        File-system locations are application-level concerns but default to previous behavior:
        - knowledge_base_path: <self._memory_path>/knowledge_base
        - chroma_persist_path: <self._memory_path>/chroma_db

        Applications should override these when integrating the SDK in different environments
        (tests, containers, ephemeral storage, etc).
        """
        super().__init__(*args, **kwargs)
        # Preserve previous default layout if _memory_path is set by the service; otherwise fallback.
        memory_root = getattr(self, "_memory_path", os.path.join(".tmp", "memory"))
        self._kb_path: str = knowledge_base_path or os.path.join(
            cast(str, memory_root),
            "knowledge_base",  # Invariant: default or _memory_path is str.
        )
        self._chroma_path: str = chroma_persist_path or os.path.join(
            cast(str, memory_root),
            "chroma_db",  # Invariant: default or _memory_path is str.
        )

    def _as_text(self, x: Any) -> str:
        """Safely coerce any object (list/dict/bytes/etc.) to text.

        This method provides a robust fallback for converting arbitrary data to a
        string. It handles None, bytes, and attempts to serialize other types as
        JSON before resorting to the standard `str()` representation, preventing
        conversion errors from propagating.

        Args:
            x: The object to convert.

        Returns:
            A string representation of the input.
        """
        if x is None:
            return ""
        if isinstance(x, str):
            return x
        if isinstance(x, bytes):
            try:
                return x.decode("utf-8", "replace")
            except Exception:
                return str(x)
        try:
            return json.dumps(x, ensure_ascii=False)
        except Exception:
            return str(x)

    def _to_text(self, x: Any) -> str:
        """Prefer joining lists of strings; otherwise fall back to JSON/str via _as_text.

        This method is designed to provide a more natural string representation for
        lists by joining their elements. For all non-list types, it delegates the
        conversion to the `_as_text` method for safe, generic handling.

        Args:
            x: The object to convert.

        Returns:
            A string representation of the input, with special handling for lists.
        """
        if isinstance(x, list):
            parts: list[str] = []
            for p in x:
                parts.append(p if isinstance(p, str) else self._as_text(p))
            return "".join(parts)
        return self._as_text(x)

    # -----------------------------
    # Diagnostics toggle
    # -----------------------------
    def _diagnostics_enabled(self) -> bool:
        """Global opt-in switch for diagnostics that may expose configuration (never full secrets)."""
        v = os.getenv("INGENIOUS_DIAGNOSTICS_ENABLED", "")
        return v.strip().lower() in {"1", "true", "yes", "on"}

    # -----------------------------
    # Instrumentation: LLM usage tracker
    # -----------------------------
    def _maybe_attach_llm_usage_logger(
        self,
        base_logger: logging.Logger,
        event_type: str,
    ) -> Optional[logging.Handler]:
        """Attach the LLM usage tracker as a logger handler if available.

        This function attempts to import and instantiate `LLMUsageTracker` from
        an optional dependency. It fails silently if the import or
        instantiation fails, ensuring that the main application flow is not
        interrupted by telemetry issues.

        Args:
            base_logger: The logger instance to which the handler will be attached.
            event_type: A string identifying the type of event being logged.

        Returns:
            The created `logging.Handler` instance on success, or `None` on failure.
        """
        try:
            # The 'ingenious' package is an optional dependency for usage telemetry.
            from ingenious.models.agent import (  # type: ignore[import-untyped]
                LLMUsageTracker as _LLMUsageTracker,
            )

            handler: logging.Handler = _LLMUsageTracker(
                agents=[],
                config=self._config,
                chat_history_repository=self._chat_service.chat_history_repository
                if self._chat_service
                else None,
                revision_id=str(uuid.uuid4()),
                identifier=str(uuid.uuid4()),
                event_type=event_type,
            )
            base_logger.addHandler(handler)
            return handler
        except Exception:
            # Telemetry is best-effort; never block main flow.
            return None

    # -----------------------------
    # Public API (non-streaming)
    # -----------------------------
    async def get_conversation_response(
        self, chat_request: ChatRequest
    ) -> ChatResponse:
        """Entry point for one-shot, non-streaming KB responses."""
        model_config = self._config.models[0]

        # Dedicated logger; applications should attach handlers to this named logger.
        base_logger = logging.getLogger(f"{EVENT_LOGGER_NAME}.kb")
        base_logger.setLevel(logging.INFO)

        # Best-effort usage telemetry
        llm_logger: Optional[logging.Handler] = self._maybe_attach_llm_usage_logger(
            base_logger, "knowledge_base"
        )

        # Build memory context (non-fatal, throttled warnings on failure).
        memory_context = await self._build_memory_context(chat_request)

        # ── Mode selection with coercion tracking ─────────────────────────────
        raw_mode_val = getattr(self._config, "knowledge_base_mode", None) or os.getenv(
            "KB_MODE", "direct"
        )
        try:
            raw_mode = str(raw_mode_val).strip().lower()
        except Exception:
            raw_mode = "direct"

        coerced = False
        if raw_mode in ("direct", "assist"):
            mode = raw_mode
        else:
            # Invalid mode → coerce to "direct" with a safety-first behavior.
            mode = "direct"
            coerced = True

        # Lazily create chat client only when needed (assist mode). Direct mode doesn't need one.
        model_client: Any | None = None

        try:
            use_azure_search = self._should_use_azure_search()

            if mode == "direct":
                # When mode is coerced, we **ignore env overrides** but still **honor per-request** overrides.
                if coerced:
                    override = (
                        self._resolve_topk_from_request(chat_request)
                        if chat_request
                        else None
                    )
                    top_k = override or _TOPK_DIRECT_DEFAULT
                else:
                    top_k = self._get_top_k("direct", chat_request)

                # Perform the policy-aware KB search.
                search_text = await self._search_knowledge_base(
                    search_query=chat_request.user_prompt,
                    use_azure_search=use_azure_search,
                    top_k=top_k,
                    logger=base_logger,
                )

                # Align header backend label to the actual result (handles Azure/Chroma).
                backend_from_result = (
                    "Azure AI Search"
                    if isinstance(search_text, str)
                    and search_text.startswith(
                        "Found relevant information from Azure AI Search"
                    )
                    else "local ChromaDB"
                    if isinstance(search_text, str)
                    and search_text.startswith(
                        "Found relevant information from ChromaDB"
                    )
                    else ("Azure AI Search" if use_azure_search else "local ChromaDB")
                )
                context = (
                    "Knowledge base search assistant using "
                    f"{backend_from_result} for finding information."
                )

                # Deterministic final message, with explicit "User question:" line.
                header = f"Context: {context}\n\n"
                if memory_context:
                    header += memory_context
                header += f"User question: {chat_request.user_prompt}\n\n"
                final_message = header + (search_text or "No response generated")

                # Token accounting (non-fatal; warns but never raises).
                total_tokens, completion_tokens = await self._safe_count_tokens(
                    system_message=self._static_system_message(memory_context),
                    user_message=chat_request.user_prompt,
                    assistant_message=final_message,
                    model=model_config.model,
                    logger=base_logger,
                )

                return ChatResponse(
                    thread_id=chat_request.thread_id or "",
                    message_id=str(uuid.uuid4()),
                    agent_response=final_message,
                    token_count=total_tokens,
                    max_token_count=completion_tokens,
                    memory_summary=final_message,
                )

            # --------- ASSIST MODE (optional) ---------
            # Use an agent to summarize/format based on tool results.
            # We need a chat client only in assist mode.
            if model_client is None:
                model_client = AzureClientFactory.create_openai_chat_completion_client(
                    model_config
                )
            use_azure_search = self._should_use_azure_search()
            search_backend = "Azure AI Search" if use_azure_search else "local ChromaDB"
            context = (
                "Knowledge base search assistant using "
                f"{search_backend} for finding information."
            )

            async def search_tool(search_query: str, topic: str = "general") -> str:
                """Tool function: Search KB using Azure or local Chroma based on policy."""
                top_k = self._get_top_k("assist", chat_request)
                return await self._search_knowledge_base(
                    search_query=search_query,
                    use_azure_search=use_azure_search,
                    top_k=top_k,
                    logger=base_logger,
                )

            search_function_tool = FunctionTool(
                search_tool,
                description=f"Search for information using {search_backend}. "
                "Use relevant keywords to find relevant information.",
            )

            system_message = self._assist_system_message(memory_context)
            search_assistant = AssistantAgent(
                name="search_assistant",
                system_message=system_message,
                model_client=model_client,
                tools=[search_function_tool],
                reflect_on_tool_use=True,
            )

            from autogen_agentchat.messages import TextMessage

            user_msg = (
                f"Context: {context}\n\nUser question: {chat_request.user_prompt}"
                if context
                else chat_request.user_prompt
            )

            cancellation_token = CancellationToken()
            response = await search_assistant.on_messages(
                messages=[TextMessage(content=user_msg, source="user")],
                cancellation_token=cancellation_token,
            )

            assistant_text = (
                self._to_text(response.chat_message.content)
                if getattr(response, "chat_message", None)
                else "No response generated"
            )

            # In assist mode we return the assistant's content verbatim.
            final_message = assistant_text

            total_tokens, completion_tokens = await self._safe_count_tokens(
                system_message=system_message,
                user_message=user_msg,
                assistant_message=final_message,
                model=model_config.model,
                logger=base_logger,
            )

            return ChatResponse(
                thread_id=chat_request.thread_id or "",
                message_id=str(uuid.uuid4()),
                agent_response=final_message,
                token_count=total_tokens,
                max_token_count=completion_tokens,
                memory_summary=final_message,
            )

        finally:
            # Always close the model client (best-effort).
            if model_client is not None:
                try:
                    await model_client.close()
                except Exception:
                    pass
            # Detach telemetry handler (best-effort).
            try:
                if llm_logger:
                    base_logger.removeHandler(llm_logger)
            except Exception:
                pass

    # -----------------------------
    # Public API (streaming)
    # -----------------------------
    async def get_streaming_conversation_response(
        self, chat_request: ChatRequest
    ) -> AsyncIterator[ChatResponseChunk]:
        """Streaming version of the knowledge base response pipeline."""
        message_id = str(uuid.uuid4())
        thread_id = chat_request.thread_id or ""

        model_config = self._config.models[0]
        base_logger = logging.getLogger(f"{EVENT_LOGGER_NAME}.kb")
        base_logger.setLevel(logging.INFO)

        # Best-effort usage telemetry
        llm_logger: Optional[logging.Handler] = self._maybe_attach_llm_usage_logger(
            base_logger, "knowledge_base"
        )

        model_client = AzureClientFactory.create_openai_chat_completion_client(
            model_config
        )

        try:
            # Initial status: "searching"
            yield ChatResponseChunk(
                thread_id=thread_id,
                message_id=message_id,
                chunk_type="status",
                content="Searching knowledge base...",
                is_final=False,
            )

            memory_context = await self._build_memory_context(chat_request)
            use_azure_search = self._should_use_azure_search()
            search_backend = "Azure AI Search" if use_azure_search else "local ChromaDB"

            # Define a tool the agent can call during streaming.
            async def search_tool(search_query: str, topic: str = "general") -> str:
                """Tool function: Search KB using Azure or local Chroma based on policy."""
                top_k = self._get_top_k("assist", chat_request)
                return await self._search_knowledge_base(
                    search_query=search_query,
                    use_azure_search=use_azure_search,
                    top_k=top_k,
                    logger=base_logger,
                )

            search_function_tool = FunctionTool(
                search_tool,
                description=f"Search for information using {search_backend}. Use relevant keywords to find relevant information.",
            )

            system_message = self._streaming_system_message(memory_context)
            search_assistant = AssistantAgent(
                name="search_assistant",
                system_message=system_message,
                model_client=model_client,
                tools=[search_function_tool],
                reflect_on_tool_use=False,  # suppress 'thinking about tools'
            )

            user_msg = f"User query: {chat_request.user_prompt}"

            # Second status: "generating"
            yield ChatResponseChunk(
                thread_id=thread_id,
                message_id=message_id,
                chunk_type="status",
                content="Generating response...",
                is_final=False,
            )

            accumulated_content = ""
            total_tokens = 0
            completion_tokens = 0

            cancellation_token = CancellationToken()

            try:

                def _looks_like_tool_chatter(text: str) -> bool:
                    # Heuristic for tool JSON or narration the model sometimes emits as plain text
                    if not text:
                        return False
                    bad_markers = (
                        '"tool_calls"',
                        '"function":{"name"',
                        '"function_call"',  # OpenAI-style
                        "Calling tool",
                        "Tool result",
                        "search_tool(",  # narrated calls
                    )
                    return any(m in text for m in bad_markers)

                def _is_tool_event(obj) -> bool:
                    # Try class name first (e.g., ToolCall*, ToolResult*)
                    cls = obj.__class__.__name__.lower()
                    if any(k in cls for k in ("tool", "functioncall", "function")):
                        return True

                    # Some streaming objects have an 'event' or 'delta' shape
                    ev = getattr(obj, "event", None)
                    if isinstance(ev, str) and any(
                        k in ev.lower() for k in ("tool", "function")
                    ):
                        return True

                    # If the object exposes a dict-like view, check common keys
                    for attr in ("tool_calls", "function_call", "tool_call_delta"):
                        if hasattr(obj, attr):
                            return True
                        d = getattr(obj, "dict", None)
                        if callable(d) and attr in (d() or {}):
                            return True
                    return False

                # Forward messages yielded by the agent's stream.
                stream = search_assistant.run_stream(
                    task=user_msg, cancellation_token=cancellation_token
                )

                async for message in stream:
                    # 1) Tool events: optionally surface a status, but don't forward noisy content
                    if _is_tool_event(message):
                        # Optional UX: show that we’re working with tools
                        yield ChatResponseChunk(
                            thread_id=thread_id,
                            message_id=message_id,
                            chunk_type="status",
                            content="Searching knowledge base...",  # or "Using tools…"
                            is_final=False,
                        )
                        continue

                    # 2) Plain text chunks
                    if hasattr(message, "content") and message.content:
                        text = str(message.content)
                        if _looks_like_tool_chatter(text):
                            # Drop narrated tool JSON/spans that sneak in as text
                            continue

                        accumulated_content += text
                        yield ChatResponseChunk(
                            thread_id=thread_id,
                            message_id=message_id,
                            chunk_type="content",
                            content=text,
                            is_final=False,
                        )

                    # 3) Token usage
                    if hasattr(message, "usage"):
                        usage = message.usage
                        if hasattr(usage, "total_tokens"):
                            total_tokens = usage.total_tokens
                        if hasattr(usage, "completion_tokens"):
                            completion_tokens = usage.completion_tokens
                        yield ChatResponseChunk(
                            thread_id=thread_id,
                            message_id=message_id,
                            chunk_type="token_count",
                            token_count=total_tokens,
                            is_final=False,
                        )

                    # 4) Final flush restoration: surface terminal TaskResult content (if any).
                    if hasattr(message, "__class__") and "TaskResult" in str(
                        message.__class__
                    ):
                        try:
                            final_msgs = getattr(message, "messages", None)
                            if final_msgs:
                                final_msg = final_msgs[-1]
                                final_text = getattr(final_msg, "content", None)
                                if final_text and final_text not in accumulated_content:
                                    if not _looks_like_tool_chatter(final_text):
                                        accumulated_content += final_text
                                        yield ChatResponseChunk(
                                            thread_id=thread_id,
                                            message_id=message_id,
                                            chunk_type="content",
                                            content=final_text,
                                            is_final=False,
                                        )
                        except Exception:
                            pass

            except Exception as e:
                # Surface a content chunk with the error (instead of failing the stream).
                base_logger.error(f"Streaming error: {e}")
                error_text = f"[Error during streaming: {str(e)}]"
                accumulated_content += error_text
                yield ChatResponseChunk(
                    thread_id=thread_id,
                    message_id=message_id,
                    chunk_type="content",
                    content=error_text,
                    is_final=False,
                )

            # Safe token-count fallback if usage wasn't reported.
            if total_tokens == 0:
                try:
                    total_tokens, completion_tokens = await self._safe_count_tokens(
                        system_message=system_message,
                        user_message=user_msg,
                        assistant_message=accumulated_content,
                        model=model_config.model,
                        logger=base_logger,
                    )
                except Exception:
                    total_tokens, completion_tokens = 0, 0

                # Rough heuristic if counter still unavailable.
                if total_tokens == 0:
                    total_tokens = (
                        len(system_message) + len(user_msg) + len(accumulated_content)
                    ) // 4
                    completion_tokens = len(accumulated_content) // 4

            # Emit the best-effort token_count update before the final chunk.
            yield ChatResponseChunk(
                thread_id=thread_id,
                message_id=message_id,
                chunk_type="token_count",
                token_count=total_tokens,
                is_final=False,
            )

            # Finalize stream with a deterministic memory summary.
            yield ChatResponseChunk(
                thread_id=thread_id,
                message_id=message_id,
                chunk_type="final",
                token_count=total_tokens,
                max_token_count=completion_tokens,
                memory_summary=(accumulated_content[:200] + "...")
                if len(accumulated_content) > 200
                else accumulated_content,
                event_type="knowledge_base_streaming",
                is_final=True,
            )

        except Exception as outer:
            # "last resort" error; still emit a terminal chunk.
            base_logger.error(f"Error in streaming knowledge base response: {outer}")
            yield ChatResponseChunk(
                thread_id=thread_id,
                message_id=message_id,
                chunk_type="error",
                content=f"An error occurred: {str(outer)}",
                is_final=True,
            )
        finally:
            try:
                await model_client.close()
            except Exception:
                pass
            # Detach telemetry handler (best-effort).
            try:
                if llm_logger:
                    base_logger.removeHandler(llm_logger)
            except Exception:
                pass

    # -----------------------------
    # Internal helpers: memory context
    # -----------------------------
    async def _build_memory_context(self, chat_request: ChatRequest) -> str:
        """Build a compact memory context from the last 10 thread messages (non-fatal)."""
        memory_context = ""
        if chat_request.thread_id and self._chat_service:
            try:
                thread_messages = await self._chat_service.chat_history_repository.get_thread_messages(
                    chat_request.thread_id
                )
                if thread_messages:
                    recent = (
                        thread_messages[-10:]
                        if len(thread_messages) > 10
                        else thread_messages
                    )
                    preview = [f"{m.role}: {m.content[:100]}..." for m in recent]
                    memory_context = (
                        "Previous conversation:\n" + "\n".join(preview) + "\n\n"
                    )
            except Exception as e:
                # Throttled warn + debug to maintain observability without noise.
                logger = logging.getLogger(f"{EVENT_LOGGER_NAME}.kb")
                now = time.monotonic()
                last = getattr(self, "_last_mem_warn_ts", 0.0)
                # Invariant: default or attribute is float.
                if (now - cast(float, last)) > 60.0:
                    logger.warning(f"Failed to retrieve thread memory: {e}")
                    self._last_mem_warn_ts = now
                else:
                    logger.debug(f"Failed to retrieve thread memory (suppressed): {e}")
        return memory_context

    # -----------------------------
    # Internal helpers: Azure availability + service lookup
    # -----------------------------
    def _is_azure_search_available(self) -> bool:
        """
        Best-effort check that the Azure Search provider/SDK is importable.
        Does not validate network/keys; runtime failures still fall back (if policy allows).
        """
        try:
            from ingenious.services.azure_search.provider import (
                AzureSearchProvider,  # type: ignore
            )

            _ = AzureSearchProvider  # silence linter
            return True
        except Exception:
            return False

    def _azure_service(self) -> Any | None:
        """Return first azure_search_services entry or None."""
        cfg = getattr(self._config, "azure_search_services", None)
        if not cfg or len(cfg) == 0:
            return None
        return cfg[0]

    def _ensure_default_azure_index(
        self, logger: Optional[logging.Logger] = None
    ) -> None:
        """
        Ensure an index_name is present for Azure service; prefer env default, otherwise a safe fallback.
        Emits INFO when env default is used; WARNING on fallback default.
        """
        service = self._azure_service()
        if not service:
            return
        idx = getattr(service, "index_name", "")
        if idx:
            return

        env_idx = os.getenv("AZURE_SEARCH_DEFAULT_INDEX")
        if env_idx:
            setattr(service, "index_name", env_idx)
            if logger:
                logger.info(
                    "Azure Search 'index_name' not configured; using env AZURE_SEARCH_DEFAULT_INDEX=%r.",
                    env_idx,
                )
            return

        default_idx = "test-index"
        setattr(service, "index_name", default_idx)
        if logger:
            logger.warning(
                "Azure Search 'index_name' not configured; using fallback default %r. "
                "Set azure_search_services[0].index_name or AZURE_SEARCH_DEFAULT_INDEX to override.",
                default_idx,
            )

    def _should_use_azure_search(self) -> bool:
        """
        Return True if Azure AI Search is configured (endpoint/key), not mocked, and SDK/provider is available.
        Missing index_name is tolerated by applying a default when needed.
        """
        service = self._azure_service()

        if not service:
            return False
        endpoint = getattr(service, "endpoint", "") or ""
        key_obj = getattr(service, "key", None) or getattr(service, "api_key", None)
        key_val = self._unwrap_secret_or_str(key_obj)
        has_creds = bool(endpoint and key_val and key_val != "mock-search-key-12345")

        if not has_creds:
            return False
        # Index name may be absent; we will fill it with a default when used.
        return self._is_azure_search_available()

    # -----------------------------
    # Debug helpers: unwrap, mask, dump KB config snapshot
    # -----------------------------
    def _unwrap_secret_or_str(self, val: Any) -> str:
        """Return the raw secret value if `val` is a secret object; else str(val)."""
        if hasattr(val, "get_secret_value"):
            try:
                return val.get_secret_value()
            except Exception:
                return ""
        return str(val) if val is not None else ""

    def _mask_secret(self, s: str | None) -> str:
        """Mask a secret: short → 'a***d'; long → 'abcd...wxyz (len=NN)'."""
        s = s or ""
        if len(s) <= 8:
            return (s[:1] + "***" + s[-1:]) if s else "<empty>"
        return f"{s[:4]}...{s[-4:]} (len={len(s)})"

    def _dump_kb_config_snapshot(
        self, logger: Optional[logging.Logger] = None
    ) -> dict[str, Any]:
        """
        Build a masked snapshot of key Azure KB settings.
        When diagnostics are enabled, write it to a YAML/plaintext file and log an INFO line.
        """
        svc = self._azure_service()
        snap: Dict[str, Any] = {}
        try:
            endpoint = (getattr(svc, "endpoint", "") or "") if svc else ""
            key_obj = (
                (getattr(svc, "key", None) or getattr(svc, "api_key", None))
                if svc
                else None
            )
            key_val = self._unwrap_secret_or_str(key_obj)
            index_name = (getattr(svc, "index_name", "") or "") if svc else ""

            env_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT", "")
            env_key = os.getenv("AZURE_SEARCH_KEY", "")
            env_index = os.getenv("AZURE_SEARCH_INDEX_NAME", "")

            snap = {
                "kb_service_endpoint": endpoint,
                "kb_service_index_name": index_name,
                "kb_service_key_masked": self._mask_secret(key_val),
                "kb_service_key_is_mock": (key_val == "mock-search-key-12345"),
                "env_AZURE_SEARCH_ENDPOINT": env_endpoint,
                "env_AZURE_SEARCH_INDEX_NAME": env_index,
                "env_AZURE_SEARCH_KEY_masked": self._mask_secret(env_key),
                "env_key_equals_service_key": (env_key == key_val)
                if env_key and key_val
                else False,
            }

            # Diagnostics are strictly opt-in; do not write files or emit config by default.
            if self._diagnostics_enabled():
                try:
                    if yaml is not None:
                        with open(
                            "Config_Values_knowldgebaseagent.yaml",
                            "w",
                            encoding="utf-8",
                        ) as f:
                            yaml.safe_dump(snap, f, sort_keys=False)
                    else:
                        with open(
                            "Config_Values_knowldgebaseagent.yaml",
                            "w",
                            encoding="utf-8",
                        ) as f:
                            for k, v in snap.items():
                                f.write(f"{k}: {v}\n")
                except Exception as write_err:
                    if logger:
                        logger.debug("Diagnostics write failed: %s", write_err)
                if logger:
                    logger.info(
                        "[KB Azure Config] endpoint=%s index=%s key=%s env_key=%s mock_key=%s",
                        endpoint,
                        index_name,
                        snap["kb_service_key_masked"],
                        snap["env_AZURE_SEARCH_KEY_masked"],
                        snap["kb_service_key_is_mock"],
                    )
        except Exception as e:
            if logger and self._diagnostics_enabled():
                logger.debug("Failed to build KB config snapshot: %s", e)
        return snap

    # -----------------------------
    # Azure preflight: split sync validation and async network check
    # -----------------------------
    def _require_valid_azure_index(
        self, logger: Optional[logging.Logger] = None
    ) -> Awaitable[None]:
        """
        Public entry point used by callers/tests.

        - Performs **synchronous** configuration validation immediately, raising:
          * PreflightError('not_configured') or
          * PreflightError('incomplete_config')
          right away (so even non-`await` callers see the error).
        - Returns an **awaitable** coroutine that, when awaited, performs the
          SDK import and network preflight. Awaiting may raise:
          * PreflightError('sdk_missing') or
          * PreflightError('preflight_failed').
        """
        endpoint, index_name, key_val = self._validate_azure_index_config(logger)
        return self._preflight_azure_index_async(endpoint, index_name, key_val, logger)

    def _validate_azure_index_config(
        self, logger: Optional[logging.Logger] = None
    ) -> Tuple[str, str, str]:
        """
        Synchronous, fail-fast validation of Azure KB config.

        Returns:
            (endpoint, index_name, key_val) if validation passes.

        Raises:
            PreflightError('not_configured') if azure service missing.
            PreflightError('incomplete_config') if endpoint/key/index missing.
        """
        # Always build a snapshot (helps even when service is missing)
        snap = self._dump_kb_config_snapshot(logger)

        service = self._azure_service()
        if not service:
            raise PreflightError(
                provider="azure_search",
                reason="not_configured",
                detail="Azure Search service missing (azure_search_services[0]).",
                snapshot=snap,
            )

        # Ensure a usable index name even if caller forgot (emits INFO/WARN).
        self._ensure_default_azure_index(logger)

        endpoint = (getattr(service, "endpoint", "") or "").strip()
        index_name = (getattr(service, "index_name", "") or "").strip()
        key_obj = getattr(service, "key", None) or getattr(service, "api_key", None)
        key_val = self._unwrap_secret_or_str(key_obj)

        # Immediate validation (raises synchronously when misconfigured).
        if not endpoint or not key_val or not index_name:
            snap = self._dump_kb_config_snapshot(logger)
            raise PreflightError(
                provider="azure_search",
                reason="incomplete_config",
                detail=(
                    f"endpoint_present={bool(endpoint)}, key_present={bool(key_val)}, "
                    f"index_name_present={bool(index_name)}"
                ),
                snapshot=snap,
            )

        return endpoint, index_name, key_val

    async def _preflight_azure_index_async(
        self,
        endpoint: str,
        index_name: str,
        key_val: str,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        """
        Asynchronous network preflight: imports SDK and verifies `get_document_count()`.
        Raises precise PreflightErrors for sdk_missing and preflight_failed.
        """
        # 1) Preserve precise reason when SDK is missing.
        try:
            from azure.search.documents.aio import (
                SearchClient as _SDKCheck,  # type: ignore[import-untyped]
            )

            _ = _SDKCheck  # silence linter
        except ImportError as e:
            raise PreflightError(
                provider="azure_search",
                reason="sdk_missing",
                detail=str(e),
                snapshot=self._dump_kb_config_snapshot(logger),
            )
        # 2) Build a short-lived client via the centralized factory.
        client = None
        try:
            cfg_stub: _SearchConfigLike = SimpleNamespace(
                search_index_name=index_name,
                search_endpoint=endpoint,
                search_key=SecretStr(key_val),
            )
            client = make_async_search_client(cfg_stub)  # no type ignore needed
        except ImportError as e:
            # If the factory or its deps are unavailable, classify as SDK missing.
            raise PreflightError(
                provider="azure_search",
                reason="sdk_missing",
                detail=str(e),
                snapshot=self._dump_kb_config_snapshot(logger),
            )
        except Exception as e:
            # Any unexpected construction failure is a preflight failure.
            raise PreflightError(
                provider="azure_search",
                reason="preflight_failed",
                detail=str(e),
                snapshot=self._dump_kb_config_snapshot(logger),
            )
        try:
            # A simple call that will 401/403 if the key or endpoint is wrong.
            await client.get_document_count()
        except PreflightError:
            # Bubble up precise errors (if any were created above).
            raise
        except Exception as e:
            raise PreflightError(
                provider="azure_search",
                reason="preflight_failed",
                detail=str(e),
                snapshot=self._dump_kb_config_snapshot(logger),
            )
        finally:
            try:
                if client:
                    await client.close()
            except Exception:
                pass

    # -----------------------------
    # Policy helpers (backend selection & behavior)
    # -----------------------------
    def _kb_policy(self) -> str:
        """
        Decide backend behavior.
        Allowed: azure_only | prefer_azure | prefer_local | local_only
        Default: azure_only (preserves strict Azure behavior).
        """
        policy = getattr(self._config, "knowledge_base_policy", None) or os.getenv(
            "KB_POLICY", "azure_only"
        )
        try:
            policy = str(policy).strip().lower()
        except Exception:
            policy = "azure_only"
        allowed = {"azure_only", "prefer_azure", "prefer_local", "local_only"}
        return policy if policy in allowed else "azure_only"

    def _fallback_on_empty(self) -> bool:
        """Return True when KB_FALLBACK_ON_EMPTY is set (1/true/yes)."""
        v = os.getenv("KB_FALLBACK_ON_EMPTY", "")
        return v.strip().lower() in {"1", "true", "yes"}

    def _azure_snippet_cap(self) -> int:
        """
        Optional cap for Azure snippet/content length.
        0 (default) keeps untrimmed behavior. Set KB_AZURE_SNIPPET_CAP=600 to trim.
        """
        v = os.getenv("KB_AZURE_SNIPPET_CAP", "")
        try:
            n = int(v)
            return max(0, n)
        except Exception:
            return 0

    # -----------------------------
    # top-k resolution helpers
    # -----------------------------
    def _resolve_topk_from_request(self, chat_request: ChatRequest) -> Optional[int]:
        """Return a positive int if the request carries an override."""
        # 1) direct attributes (kb_top_k, top_k, search_top_k)
        for attr in ("kb_top_k", "top_k", "search_top_k"):
            val = getattr(chat_request, attr, None)
            try:
                if isinstance(val, int) and val > 0:
                    return int(val)
                if isinstance(val, str) and val.strip().isdigit() and int(val) > 0:
                    return int(val)
            except Exception:
                pass
        # 2) nested parameters dict (kb_top_k, top_k, search_top_k)
        params = getattr(chat_request, "parameters", None)
        if isinstance(params, dict):
            for key in ("kb_top_k", "top_k", "search_top_k"):
                val = params.get(key)
                try:
                    if isinstance(val, int) and val > 0:
                        return int(val)
                    if isinstance(val, str) and val.strip().isdigit() and int(val) > 0:
                        return int(val)
                except Exception:
                    pass
        return None

    def _get_top_k(self, mode: str, chat_request: Optional[ChatRequest]) -> int:
        """Priority: request override → env override → safe defaults."""
        # 1) per-request (always highest priority)
        if chat_request is not None:
            override = self._resolve_topk_from_request(chat_request)
            if override:
                return override
        # 2) env override (only if mode is valid and not coerced)
        if mode == "assist":
            env_v = (os.getenv("KB_TOPK_ASSIST") or "").strip()
            if env_v.isdigit() and int(env_v) > 0:
                return int(env_v)
            return _TOPK_ASSIST_DEFAULT
        else:
            env_v = (os.getenv("KB_TOPK_DIRECT") or "").strip()
            if env_v.isdigit() and int(env_v) > 0:
                return int(env_v)
            return _TOPK_DIRECT_DEFAULT

    # -----------------------------
    # Backend search (policy-aware)
    # -----------------------------
    async def _search_knowledge_base(
        self,
        search_query: str,
        use_azure_search: bool,
        top_k: int,
        logger: Optional[logging.Logger] = None,
    ) -> str:
        """
        Policy-aware unified search that chooses Azure or Chroma as needed,
        with optional fallbacks based on KB_POLICY and KB_FALLBACK_ON_EMPTY.
        """
        if logger:
            logger.debug(
                "[KB] search start policy=%s use_azure=%s top_k=%s query=%r",
                self._kb_policy(),
                use_azure_search,
                top_k,
                search_query[:200],
            )

        policy = self._kb_policy()

        # Local-only short-circuit.
        if policy == "local_only":
            return await self._search_local_chroma(search_query, top_k, logger)

        # Handle prefer_local policy
        prefer_local_needs_azure = False
        if policy == "prefer_local":
            result = await self._handle_prefer_local_policy(
                search_query, use_azure_search, top_k, logger
            )
            if result is not None:
                return result
            # If we get here, prefer_local needs Azure fallback
            prefer_local_needs_azure = True

        # Determine if Azure should be attempted
        attempt_azure = self._should_attempt_azure(
            policy, use_azure_search, prefer_local_needs_azure
        )

        # Try Azure search if applicable
        if attempt_azure:
            result = await self._try_azure_search(search_query, top_k, policy, logger)
            if result is not None:
                return result

        # Handle fallback scenarios
        return await self._handle_search_fallback(
            search_query, top_k, policy, use_azure_search, logger
        )

    async def _handle_prefer_local_policy(
        self,
        search_query: str,
        use_azure_search: bool,
        top_k: int,
        logger: Optional[logging.Logger],
    ) -> Optional[str]:
        """Handle prefer_local policy: try Chroma first, optionally fall back to Azure."""
        local_result = await self._search_local_chroma(search_query, top_k, logger)
        if not (
            self._fallback_on_empty()
            and local_result.startswith("No relevant information")
        ):
            return local_result
        # Returns None to indicate Azure fallback should be attempted
        return None

    def _should_attempt_azure(
        self,
        policy: str,
        use_azure_search: bool,
        prefer_local_needs_azure: bool = False,
    ) -> bool:
        """Determine if Azure search should be attempted based on policy."""
        if prefer_local_needs_azure:
            return use_azure_search
        return policy in {"azure_only", "prefer_azure"} and use_azure_search

    async def _try_azure_search(
        self,
        search_query: str,
        top_k: int,
        policy: str,
        logger: Optional[logging.Logger],
    ) -> Optional[str]:
        """Attempt Azure search with error handling and fallback logic."""
        last_err: Optional[Exception] = None
        provider: Any = None  # Will be AzureSearchProvider when imported

        try:
            # Diagnostics & preflight
            self._dump_kb_config_snapshot(logger)
            await self._require_valid_azure_index(logger)

            # Create provider and execute search
            from ingenious.services.azure_search.provider import (
                AzureSearchProvider,
            )  # type: ignore

            provider = AzureSearchProvider(self._config)

            # Execute Azure search
            azure_result = await self._execute_azure_search_with_provider(
                provider, search_query, top_k
            )

            # Check for prefer_azure fallback
            if self._should_fallback_from_azure(policy, azure_result):
                if logger:
                    logger.warning(
                        "Azure returned no results; falling back to ChromaDB (KB_FALLBACK_ON_EMPTY=1)."
                    )
                self._ensure_kb_directory()
                return await self._search_local_chroma(search_query, top_k, logger)

            return azure_result

        except ImportError as e:
            last_err = e
            self._handle_azure_import_error(e, policy, logger)
        except PreflightError as e:
            last_err = e
            self._handle_azure_preflight_error(e, policy, logger)
        except Exception as e:
            last_err = e
            self._handle_azure_general_error(e, policy, logger)
        finally:
            await self._close_azure_provider(provider)

        # Store the error for later use if needed
        self._last_azure_error = last_err
        return None

    async def _execute_azure_search_with_provider(
        self,
        provider: Any,
        search_query: str,
        top_k: int,
    ) -> str:
        """Execute Azure search using provided provider and format results."""
        chunks: List[Dict[str, Any]] = await provider.retrieve(
            search_query, top_k=top_k
        )

        if not chunks:
            return f"No relevant information found in Azure AI Search for query: {search_query}"

        return self._format_azure_results(chunks)

    def _format_azure_results(self, chunks: List[Dict[str, Any]]) -> str:
        """Format Azure search results into readable string."""
        parts: List[str] = []
        cap = self._azure_snippet_cap()

        for i, c in enumerate(chunks, 1):
            formatted_chunk = self._format_single_chunk(i, c, cap)
            parts.append(formatted_chunk)

        return (
            "Found relevant information from Azure AI Search:\n\n"
            + "\n\n---\n\n".join(parts)
        )

    def _format_single_chunk(self, index: int, chunk: Dict[str, Any], cap: int) -> str:
        """Format a single search result chunk."""
        title = chunk.get("title", chunk.get("id", f"Source {index}"))
        score = chunk.get("_final_score", "")
        snippet = chunk.get("snippet", "") or ""
        content = chunk.get("content", "") or ""

        if cap > 0:
            snippet = cast(str, snippet)[:cap]
            content = cast(str, content)[:cap]

        lines: list[str] = []
        if snippet:
            lines.append(cast(str, snippet))
        if content and content != snippet:
            lines.append(cast(str, content))
        body = "\n".join(lines) if lines else ""

        return f"[{index}] {title} (score={score})\n{body}"

    def _should_fallback_from_azure(self, policy: str, azure_result: str) -> bool:
        """Check if we should fallback from Azure to local based on policy and result."""
        return (
            policy == "prefer_azure"
            and self._fallback_on_empty()
            and azure_result.startswith("No relevant information")
        )

    def _handle_azure_import_error(
        self,
        error: ImportError,
        policy: str,
        logger: Optional[logging.Logger],
    ) -> None:
        """Handle Azure import errors based on policy."""
        if policy == "azure_only":
            raise PreflightError(
                provider="azure_search",
                reason="sdk_missing",
                detail="Azure Search SDK/provider not available; retrieval is disabled by policy.",
                snapshot=self._dump_kb_config_snapshot(logger),
            )
        if logger:
            logger.warning(
                "Azure SDK/provider not available; falling back to ChromaDB."
            )

    def _handle_azure_preflight_error(
        self,
        error: PreflightError,
        policy: str,
        logger: Optional[logging.Logger],
    ) -> None:
        """Handle Azure preflight errors based on policy."""
        if policy == "azure_only":
            raise error
        if logger:
            logger.warning(
                "Azure validation failed (%s); falling back to ChromaDB.", error
            )

    def _handle_azure_general_error(
        self,
        error: Exception,
        policy: str,
        logger: Optional[logging.Logger],
    ) -> None:
        """Handle general Azure errors based on policy."""
        if policy == "azure_only":
            raise PreflightError(
                provider="azure_search",
                reason="provider_failed",
                detail=str(error),
                snapshot=self._dump_kb_config_snapshot(logger),
            )
        if logger:
            logger.warning(
                "Azure provider failed (%s); falling back to ChromaDB.", error
            )

    async def _close_azure_provider(self, provider: Optional[Any]) -> None:
        """Safely close Azure provider if it exists."""
        if provider:
            try:
                await provider.close()
            except Exception:
                pass

    def _ensure_kb_directory(self) -> None:
        """Ensure the KB directory exists for local retrieval."""
        try:
            os.makedirs(self._kb_path, exist_ok=True)
        except Exception:
            pass

    async def _handle_search_fallback(
        self,
        search_query: str,
        top_k: int,
        policy: str,
        use_azure_search: bool,
        logger: Optional[logging.Logger],
    ) -> str:
        """Handle fallback scenarios when Azure search wasn't used or failed."""
        # Check if we can fallback to local
        if policy in {"prefer_azure", "prefer_local"} or (
            policy != "azure_only" and not use_azure_search
        ):
            self._ensure_kb_directory()
            return await self._search_local_chroma(search_query, top_k, logger)

        # Azure-only but Azure wasn't available/allowed
        if policy == "azure_only" and not use_azure_search:
            raise PreflightError(
                provider="azure_search",
                reason="policy",
                detail="Azure Search is required for knowledge base retrieval and must not fall back to local stores.",
                snapshot=self._dump_kb_config_snapshot(logger),
            )

        # Surface the last Azure error if present
        if hasattr(self, "_last_azure_error") and self._last_azure_error:
            raise PreflightError(
                provider="azure_search",
                reason="unknown",
                detail=str(self._last_azure_error),
                snapshot=self._dump_kb_config_snapshot(logger),
            )

        # Fallback final message
        return f"No relevant information found in Azure AI Search for query: {search_query}"

    # -----------------------------
    # Local Chroma path
    # -----------------------------
    async def _search_local_chroma(
        self,
        search_query: str,
        top_k: int,
        logger: Optional[logging.Logger] = None,
    ) -> str:
        """
        Local ChromaDB search (used directly or as a fallback).
        Returns short, user-friendly messages while logging details server-side.
        """
        knowledge_base_path = self._kb_path
        chroma_path = self._chroma_path

        # If the knowledge base folder doesn't exist, log the path and return a concise user-facing message.
        if not os.path.exists(knowledge_base_path):
            if logger:
                logger.warning(
                    "Knowledge base directory missing/empty: %s", knowledge_base_path
                )
            # Actionable guidance with dynamic, trailing-slash path.
            kb_display = knowledge_base_path
            if not kb_display.endswith(os.sep):
                kb_display = kb_display + os.sep
            return f"Error: Knowledge base directory is empty. Please add documents to {kb_display}"

        # Try to import ChromaDB; provide an explicit install hint on failure.
        try:
            import chromadb  # type: ignore[import-untyped]
        except ImportError:
            return "Error: ChromaDB not installed. Please install with: uv add chromadb"

        client = chromadb.PersistentClient(path=chroma_path)
        collection_name = "knowledge_base"

        # Open/create the collection; on first creation, ingest docs from disk.
        try:
            collection = client.get_collection(name=collection_name)
        except Exception:
            collection = client.create_collection(name=collection_name)
            docs, ids = await self._read_kb_documents_offthread(knowledge_base_path)
            if docs:
                try:
                    collection.add(documents=docs, ids=ids)
                except Exception as e:
                    if logger:
                        logger.warning(f"ChromaDB add() failed: {e}")
            else:
                # Explicit, concise message when the directory has no usable documents.
                return "Error: No documents found in knowledge base directory"

        # Execute the query; surface a short "Search error" message on failure.
        try:
            results = collection.query(query_texts=[search_query], n_results=top_k)
        except Exception as e:
            if logger:
                logger.error(f"ChromaDB query failed: {e}")
            return f"Search error: {str(e)}"

        # Format results if any; otherwise report "No relevant information".
        docs = results.get("documents") or []
        if docs and docs[0]:
            return "Found relevant information from ChromaDB:\n\n" + "\n\n".join(
                docs[0]
            )

        return f"No relevant information found in ChromaDB for query: {search_query}"

    # -----------------------------
    # File I/O helpers (off-thread)
    # -----------------------------
    async def _read_kb_documents_offthread(
        self, kb_path: str
    ) -> Tuple[List[str], List[str]]:
        """Read .md/.txt documents from disk off-thread to avoid blocking the event loop."""

        def _read() -> Tuple[List[str], List[str]]:
            """Helper to perform the blocking file I/O operations."""
            documents: List[str] = []
            ids: List[str] = []
            for filename in os.listdir(kb_path):
                if filename.endswith((".md", ".txt")):
                    filepath = os.path.join(kb_path, filename)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()
                    except Exception:
                        continue
                    # Simple blank-line chunking; preserves predictable chunk IDs.
                    chunks = content.split("\n\n")
                    for i, chunk in enumerate(chunks):
                        chunk = chunk.strip()
                        if chunk:
                            documents.append(chunk)
                            ids.append(f"{filename}_chunk_{i}")
            return documents, ids

        return await asyncio.to_thread(_read)

    # -----------------------------
    # Token accounting (defensive)
    # -----------------------------
    async def _safe_count_tokens(
        self,
        system_message: str,
        user_message: str,
        assistant_message: str,
        model: str,
        logger: Optional[logging.Logger] = None,
    ) -> Tuple[int, int]:
        """Compute token counts defensively; never fail the request."""
        try:
            from ingenious.utils.token_counter import num_tokens_from_messages

            msgs: list[dict[str, Any]] = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": assistant_message},
            ]
            total = num_tokens_from_messages(msgs, model)
            prompt = num_tokens_from_messages(msgs[:-1], model)
            completion = total - prompt
            return total, completion
        except Exception as e:
            if logger:
                logger.warning(f"Token counting failed: {e}")
            return 0, 0

    # -----------------------------
    # System prompts (static text)
    # -----------------------------
    def _static_system_message(self, memory_context: str) -> str:
        """Deterministic system prompt for direct mode."""
        prefix = "You are a knowledge base search assistant that uses Azure AI Search or local ChromaDB.\n\n"
        if memory_context:
            prefix += memory_context
        prefix += (
            "Always base your responses on knowledge base search results. "
            "If nothing is found, clearly state that and suggest rephrasing the query. "
            "TERMINATE your response when the task is complete."
        )
        return prefix

    def _assist_system_message(self, memory_context: str) -> str:
        """Richer prompt for assist mode (summarization + guidelines + citation hint)."""
        parts = [
            "You are a knowledge base search assistant that can use both Azure AI Search and local ChromaDB storage.\n",
        ]
        if memory_context:
            parts.append(memory_context)

        parts.append(
            "IMPORTANT: If there is previous conversation context above, you MUST:\n"
            "- Reference it when answering follow-up questions\n"
            "- Use information from previous searches to inform new searches\n"
            "- Maintain context about what information has already been discussed\n"
            '- Answer questions that refer to "it", "that", "those" etc. based on previous context\n\n'
            "Tasks:\n"
            "- Help users find information by searching the knowledge base\n"
            "- Use the search_tool to look up information\n"
            "- Always base your responses on search results from the knowledge base\n"
            "- Always consider and reference previous conversation when relevant\n"
            "- If no information is found, clearly state that and suggest rephrasing the query\n\n"
            "Guidelines for search queries:\n"
            "- Use specific, relevant keywords\n"
            "- Try different phrasings if initial search doesn't return results\n"
            "- Focus on topics that are relevant to the knowledge base content\n\n"
            "Format your responses clearly and cite the knowledge base when providing information.\n"
            "TERMINATE your response when the task is complete."
        )
        return "".join(parts)

    def _streaming_system_message(self, memory_context: str) -> str:
        """
        Streaming prompt with guidance, topics, and citation directive.
        """
        parts: List[str] = [
            "You are a knowledge base search assistant that can use both Azure AI Search and local ChromaDB storage.\n\n"
        ]
        if memory_context:
            parts.append(memory_context)

        parts.append(
            "IMPORTANT: Maintain context and base your responses on search results.\n\n"
            "Guidelines for search queries:\n"
            "- Use specific, relevant keywords\n"
            "- Try different phrasings if initial search doesn't return results\n"
            "- Focus on topics that are relevant to the knowledge base content\n\n"
            "Knowledge base contains documents about:\n"
            "- Azure configuration and setup\n"
            "- Workplace safety guidelines\n"
            "- Health information and nutrition\n"
            "- Emergency procedures\n"
            "- Mental health and wellbeing\n"
            "- First aid basics\n"
            "- General informational content\n\n"
            "Format your responses clearly and cite the knowledge base when providing information."
        )
        return "".join(parts)
