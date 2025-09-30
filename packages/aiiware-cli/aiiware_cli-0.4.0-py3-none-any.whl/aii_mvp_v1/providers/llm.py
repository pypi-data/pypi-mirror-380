"""LLM provider integration using Pydantic AI."""

import os
from typing import Any
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.openai import OpenAIModel

from ..core.models import LLMRequest, LLMResponse, TaskType, Provider


class LLMService:
    """Service for interacting with LLM providers."""

    def __init__(self):
        self.agents: dict[Provider, Agent] = {}
        self._setup_providers()

    def _setup_providers(self) -> None:
        """Set up available LLM providers."""
        # Anthropic
        if os.getenv("ANTHROPIC_API_KEY"):
            model = AnthropicModel("claude-3-5-sonnet-20241022")
            self.agents[Provider.ANTHROPIC] = Agent(model)

        # OpenAI
        if os.getenv("OPENAI_API_KEY"):
            model = OpenAIModel("gpt-4")
            self.agents[Provider.OPENAI] = Agent(model)

    def _build_prompt(self, request: LLMRequest) -> str:
        """Build a prompt based on the task type."""
        base_prompt = f"User request: {request.user_input}\\n\\n"

        if request.task_type == TaskType.TRANSLATION:
            return base_prompt + "Please translate the given text accurately. Provide only the translation."
        elif request.task_type == TaskType.EXPLANATION:
            return base_prompt + "Please provide a clear, helpful explanation."
        elif request.task_type == TaskType.CODING:
            return base_prompt + "Please help with this coding request. Provide code with explanations."
        else:
            return base_prompt + "Please help with this request."

    async def process_request(self, request: LLMRequest) -> LLMResponse:
        """Process an LLM request."""
        if request.provider not in self.agents:
            raise ValueError(f"Provider {request.provider.value} not available. Please set up API keys.")

        agent = self.agents[request.provider]
        prompt = self._build_prompt(request)

        try:
            result = await agent.run(prompt)
            # Extract content from Pydantic AI result
            if hasattr(result, 'output'):
                content = result.output
            elif hasattr(result, 'data'):
                content = result.data
            else:
                content = str(result)

            return LLMResponse(
                content=content,
                model_used=request.model,
                provider_used=request.provider.value
            )
        except Exception as e:
            raise RuntimeError(f"LLM request failed: {e}")

    def get_available_providers(self) -> list[Provider]:
        """Get list of available providers."""
        return list(self.agents.keys())