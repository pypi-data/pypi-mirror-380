from __future__ import annotations

from typing import TYPE_CHECKING, assert_never, overload

from omniadapters.core.models import (
    AnthropicProviderConfig,
    AzureOpenAIProviderConfig,
    GeminiProviderConfig,
    OpenAIProviderConfig,
)
from omniadapters.structify.adapters.anthropic import AnthropicAdapter
from omniadapters.structify.adapters.azure_openai import AzureOpenAIAdapter
from omniadapters.structify.adapters.gemini import GeminiAdapter
from omniadapters.structify.adapters.openai import OpenAIAdapter

if TYPE_CHECKING:
    from omniadapters.core.models import (
        AnthropicCompletionClientParams,
        AzureOpenAICompletionClientParams,
        CompletionClientParams,
        GeminiCompletionClientParams,
        OpenAICompletionClientParams,
        ProviderConfig,
    )
    from omniadapters.structify.models import InstructorConfig


@overload
def create_adapter(
    *,
    provider_config: OpenAIProviderConfig,
    completion_params: OpenAICompletionClientParams,
    instructor_config: InstructorConfig,
) -> OpenAIAdapter: ...


@overload
def create_adapter(
    *,
    provider_config: AnthropicProviderConfig,
    completion_params: AnthropicCompletionClientParams,
    instructor_config: InstructorConfig,
) -> AnthropicAdapter: ...


@overload
def create_adapter(
    *,
    provider_config: GeminiProviderConfig,
    completion_params: GeminiCompletionClientParams,
    instructor_config: InstructorConfig,
) -> GeminiAdapter: ...


@overload
def create_adapter(
    *,
    provider_config: AzureOpenAIProviderConfig,
    completion_params: AzureOpenAICompletionClientParams,
    instructor_config: InstructorConfig,
) -> AzureOpenAIAdapter: ...


@overload
def create_adapter(
    *,
    provider_config: ProviderConfig,
    completion_params: CompletionClientParams,
    instructor_config: InstructorConfig,
) -> OpenAIAdapter | AnthropicAdapter | GeminiAdapter | AzureOpenAIAdapter: ...


def create_adapter(
    *,
    provider_config: ProviderConfig,
    completion_params: CompletionClientParams,
    instructor_config: InstructorConfig,
) -> OpenAIAdapter | AnthropicAdapter | GeminiAdapter | AzureOpenAIAdapter:
    match provider_config:
        case OpenAIProviderConfig():
            return OpenAIAdapter(
                provider_config=provider_config,
                completion_params=completion_params,
                instructor_config=instructor_config,
            )
        case AnthropicProviderConfig():
            return AnthropicAdapter(
                provider_config=provider_config,
                completion_params=completion_params,
                instructor_config=instructor_config,
            )
        case GeminiProviderConfig():
            return GeminiAdapter(
                provider_config=provider_config,
                completion_params=completion_params,
                instructor_config=instructor_config,
            )
        case AzureOpenAIProviderConfig():
            return AzureOpenAIAdapter(
                provider_config=provider_config,
                completion_params=completion_params,
                instructor_config=instructor_config,
            )
        case _:
            assert_never(provider_config)
