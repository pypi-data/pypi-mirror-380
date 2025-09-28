"""Documentation: https://docs.claude.com/en/api/messages"""

from __future__ import annotations

from typing import Any, AsyncIterator, Literal, overload

from anthropic import AsyncAnthropic
from anthropic.types import Message, RawMessageStreamEvent
from anthropic.types import MessageParam as AnthropicMessageParam
from instructor import Mode

from omniadapters.completion.adapters.base import BaseAdapter
from omniadapters.core.models import AnthropicProviderConfig, CompletionResponse, CompletionUsage, StreamChunk
from omniadapters.core.types import MessageParam


class AnthropicAdapter(
    BaseAdapter[
        AnthropicProviderConfig,
        AsyncAnthropic,
        AnthropicMessageParam,
        Message,
        RawMessageStreamEvent,
    ]
):
    @property
    def instructor_mode(self) -> Mode:
        return Mode.ANTHROPIC_TOOLS

    def _create_client(self) -> AsyncAnthropic:
        config_dict = self.provider_config.model_dump()
        return AsyncAnthropic(**config_dict)

    @overload
    async def _agenerate(
        self,
        messages: list[MessageParam],
        *,
        stream: Literal[False] = False,
        **kwargs: Any,
    ) -> Message: ...

    @overload
    async def _agenerate(
        self,
        messages: list[MessageParam],
        *,
        stream: Literal[True],
        **kwargs: Any,
    ) -> AsyncIterator[RawMessageStreamEvent]: ...

    async def _agenerate(
        self,
        messages: list[MessageParam],
        *,
        stream: bool = False,
        **kwargs: Any,
    ) -> Message | AsyncIterator[RawMessageStreamEvent]:
        formatted_params = self._thanks_instructor(messages, **kwargs)
        # NOTE: least overload needed requires model and max_tokens!
        response = await self.client.messages.create(
            # messages=formatted_messages,
            # model=self.completion_params.model,
            # max_tokens=kwargs.pop("max_tokens", 1024),  # NOTE: anthropic requires `max_tokens` to be specified
            stream=stream,
            **formatted_params,
        )

        return response

    def _to_unified_response(self, response: Message) -> CompletionResponse[Message]:
        content = ""
        if response.content:
            for block in response.content:
                text_val = getattr(block, "text", None)
                if isinstance(text_val, str):
                    content += text_val

        return CompletionResponse[Message](
            content=content,
            model=response.model,
            usage=CompletionUsage(
                prompt_tokens=response.usage.input_tokens,
                completion_tokens=response.usage.output_tokens,
                total_tokens=response.usage.input_tokens + response.usage.output_tokens,
            )
            if response.usage
            else None,
            raw_response=response,
        )

    def _to_unified_chunk(self, chunk: RawMessageStreamEvent) -> StreamChunk | None:
        if chunk.type == "content_block_delta":
            delta = getattr(chunk, "delta", None)

            text_val = getattr(delta, "text", None)
            if isinstance(text_val, str):
                return StreamChunk(
                    content=text_val,
                    raw_chunk=chunk,
                )

            partial_json = getattr(delta, "partial_json", None)
            if partial_json is not None:
                return StreamChunk(
                    content="",
                    tool_calls=[{"partial_json": partial_json}],
                    raw_chunk=chunk,
                )

        elif chunk.type == "content_block_start":
            content_block = getattr(chunk, "content_block", None)
            if content_block:
                block_type = getattr(content_block, "type", None)
                if block_type == "tool_use":
                    tool_name = getattr(content_block, "name", None)
                    tool_id = getattr(content_block, "id", None)
                    return StreamChunk(
                        content="",
                        tool_calls=[{"type": "tool_use", "name": tool_name, "id": tool_id}],
                        raw_chunk=chunk,
                    )

        elif chunk.type == "message_stop":
            return StreamChunk(
                content="",
                finish_reason="stop",
                raw_chunk=chunk,
            )
        return None
