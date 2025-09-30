"""Pydantic AI-based LLM Provider - Modern agent framework integration"""

from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any

from pydantic_ai import Agent
from pydantic_ai.models import Model, infer_model

from .llm_provider import LLMProvider, LLMResponse


@dataclass
class PydanticAIResponse:
    """Enhanced response with Pydantic AI integration"""

    content: str
    model: str
    usage: dict[str, int] = None
    finish_reason: str = "stop"
    run_id: str = None


class PydanticAIProvider(LLMProvider):
    """Pydantic AI-powered LLM provider with modern agent capabilities"""

    def __init__(self, api_key: str, model_name: str = "gpt-4"):
        super().__init__(api_key, model_name)
        self._model: Model = None
        self._agent: Agent = None
        self._underlying_provider_name: str = model_name  # Store the underlying provider info
        self._initialize_client()

    def _initialize_client(self):
        """Initialize Pydantic AI model and agent"""
        try:
            # Infer the model from the model name
            self._model = infer_model(self.model)

            # Create a basic agent for text completion
            self._agent = Agent(
                model=self._model,
                system_prompt="You are a helpful AI assistant that provides accurate and concise responses.",
            )

        except Exception as e:
            raise RuntimeError(
                f"Failed to initialize Pydantic AI provider: {str(e)}"
            ) from e

    @property
    def provider_name(self) -> str:
        """Get the underlying provider name for display"""
        return self._underlying_provider_name

    @property
    def model_info(self) -> str:
        """Get formatted model information"""
        return f"PydanticAI:{self.model}"

    async def complete(self, prompt: str, **kwargs) -> str:
        """Generate completion from prompt using Pydantic AI"""
        if not self._agent:
            raise RuntimeError("Pydantic AI agent not initialized")

        try:
            # Run the agent with the prompt
            result = await self._agent.run(prompt)
            return result.output

        except Exception as e:
            raise RuntimeError(f"Pydantic AI completion failed: {str(e)}") from e

    async def complete_with_usage(self, prompt: str, **kwargs) -> LLMResponse:
        """Generate completion with detailed usage information using Pydantic AI"""
        if not self._agent:
            raise RuntimeError("Pydantic AI agent not initialized")

        try:
            # Run the agent with the prompt
            result = await self._agent.run(prompt)

            # Extract usage information from the result
            usage = {}

            # Call the usage() method to get actual usage data
            usage_data = None
            if hasattr(result, "usage"):
                try:
                    usage_data = result.usage()  # Call the method!
                except Exception as e:
                    # Fallback if usage() method fails
                    pass

            if usage_data:
                # Pydantic AI usage structure may vary
                if hasattr(usage_data, "request_tokens"):
                    usage["input_tokens"] = usage_data.request_tokens or 0
                elif hasattr(usage_data, "input_tokens"):
                    usage["input_tokens"] = usage_data.input_tokens or 0

                if hasattr(usage_data, "response_tokens"):
                    usage["output_tokens"] = usage_data.response_tokens or 0
                elif hasattr(usage_data, "output_tokens"):
                    usage["output_tokens"] = usage_data.output_tokens or 0

                if hasattr(usage_data, "total_tokens"):
                    usage["total_tokens"] = usage_data.total_tokens or 0
                else:
                    # Calculate total if not available
                    usage["total_tokens"] = usage.get("input_tokens", 0) + usage.get(
                        "output_tokens", 0
                    )
            else:
                print("DEBUG: Using fallback token estimation")
                # Fallback: estimate token usage
                input_estimate = len(prompt.split()) * 1.3
                output_estimate = (
                    len(result.output.split()) * 1.3
                    if isinstance(result.output, str)
                    else 0
                )
                print(f"DEBUG: Input estimate: {input_estimate} (prompt words: {len(prompt.split())})")
                print(f"DEBUG: Output estimate: {output_estimate} (result words: {len(result.output.split()) if isinstance(result.output, str) else 0})")
                usage = {
                    "input_tokens": int(input_estimate),
                    "output_tokens": int(output_estimate),
                    "total_tokens": int(input_estimate + output_estimate),
                }
                print(f"DEBUG: Final estimated usage: {usage}")

            return LLMResponse(
                content=result.output,
                model=self.model,
                usage=usage,
                finish_reason="stop",
            )

        except Exception as e:
            # Add debug information
            print(f"Debug: Pydantic AI error: {type(e).__name__}: {str(e)}")
            if hasattr(e, "__dict__"):
                print(f"Debug: Error attributes: {e.__dict__}")
            raise RuntimeError(
                f"Pydantic AI completion with usage failed: {str(e)}"
            ) from e

    async def complete_with_tools(
        self,
        messages: list[dict[str, str]],
        tools: list[dict[str, Any]] = None,
        **kwargs,
    ) -> dict[str, Any]:
        """Generate completion with function calling support"""
        # For now, convert to simple completion
        # TODO: Implement proper tool calling with Pydantic AI tools
        if messages:
            last_message = messages[-1]
            if last_message.get("role") == "user":
                result = await self.complete_with_usage(
                    last_message["content"], **kwargs
                )
                return {
                    "content": result.content,
                    "usage": result.usage,
                    "finish_reason": result.finish_reason,
                }

        return {"content": "", "usage": {}, "finish_reason": "stop"}

    async def stream_complete(self, prompt: str, **kwargs) -> AsyncIterator[str]:
        """Stream completion from prompt using Pydantic AI"""
        if not self._agent:
            raise RuntimeError("Pydantic AI agent not initialized")

        try:
            # Use Pydantic AI streaming support
            async with self._agent.run_stream(prompt) as stream:
                async for message in stream:
                    # Handle different message types from Pydantic AI stream
                    if hasattr(message, "snapshot"):
                        # This is a streaming event with partial content
                        if (
                            hasattr(message.snapshot, "all_messages")
                            and message.snapshot.all_messages
                        ):
                            last_message = message.snapshot.all_messages[-1]
                            if (
                                hasattr(last_message, "content")
                                and last_message.content
                            ):
                                yield last_message.content
                    elif hasattr(message, "content") and message.content:
                        # Direct content message
                        yield message.content
                    elif hasattr(message, "delta") and message.delta:
                        # Delta content (incremental updates)
                        yield message.delta

        except Exception as e:
            # Fallback to regular completion if streaming fails
            try:
                result = await self.complete(prompt, **kwargs)
                yield result
            except Exception as fallback_error:
                raise RuntimeError(
                    f"Both streaming and fallback completion failed. Streaming: {str(e)}, Fallback: {str(fallback_error)}"
                ) from e

    async def close(self) -> None:
        """Close provider connections"""
        # Pydantic AI handles cleanup automatically
        pass


def create_pydantic_ai_provider(
    provider_name: str, api_key: str, model: str
) -> PydanticAIProvider:
    """Factory function to create Pydantic AI providers"""

    # Map provider names to model strings that Pydantic AI understands
    model_mapping = {
        "openai": {
            "gpt-4": "openai:gpt-4",
            "gpt-4-turbo": "openai:gpt-4-turbo-preview",
            "gpt-3.5-turbo": "openai:gpt-3.5-turbo",
        },
        "anthropic": {
            "claude-3-5-sonnet-20241022": "anthropic:claude-3-5-sonnet-20241022",
            "claude-3-5-haiku-20241022": "anthropic:claude-3-5-haiku-20241022",
            "claude-3-opus-20240229": "anthropic:claude-3-opus-20240229",
            "claude-3-7-sonnet-20250219": "anthropic:claude-3-7-sonnet-20250219",
        },
        "gemini": {
            "gemini-2.0-flash": "gemini-2.0-flash-exp",
            "gemini-1.5-pro": "gemini-1.5-pro",
            "gemini-1.5-flash": "gemini-1.5-flash",
        },
    }

    # Get the appropriate model string with improved fallback logic
    provider_models = model_mapping.get(provider_name.lower(), {})

    if model in provider_models:
        # Model found in mapping - use the mapped value
        pydantic_model = provider_models[model]
    else:
        # Model not in mapping - use the configured model directly with provider prefix
        # This allows for new models that aren't in our mapping yet
        pydantic_model = f"{provider_name.lower()}:{model}"

    # Set API key in environment for Pydantic AI
    import os

    if provider_name.lower() == "openai":
        os.environ["OPENAI_API_KEY"] = api_key
    elif provider_name.lower() == "anthropic":
        os.environ["ANTHROPIC_API_KEY"] = api_key
    elif provider_name.lower() == "gemini":
        os.environ["GEMINI_API_KEY"] = api_key

    return PydanticAIProvider(api_key, pydantic_model)
