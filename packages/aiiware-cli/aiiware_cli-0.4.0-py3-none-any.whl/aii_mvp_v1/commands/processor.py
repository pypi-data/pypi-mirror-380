"""Command processing and task detection."""

import re
from typing import Any

from ..core.models import LLMRequest, TaskType, Provider


class CommandProcessor:
    """Processes user commands and detects task types."""

    def __init__(self):
        self.translation_patterns = [
            r"translate\s+(.+?)\s+to\s+(\w+)",
            r"translate\s+(.+?)\s+from\s+(\w+)\s+to\s+(\w+)",
            r"(.+?)\s+in\s+(\w+)",
        ]

        self.explanation_patterns = [
            r"explain\s+(.+)",
            r"what\s+is\s+(.+)",
            r"how\s+does\s+(.+)\s+work",
        ]

        self.coding_patterns = [
            r"write\s+(.+?)\s+function",
            r"code\s+(.+)",
            r"implement\s+(.+)",
        ]

    def detect_task_type(self, user_input: str) -> TaskType:
        """Detect the type of task from user input."""
        user_input_lower = user_input.lower()

        # Check for translation patterns
        for pattern in self.translation_patterns:
            if re.search(pattern, user_input_lower):
                return TaskType.TRANSLATION

        # Check for explanation patterns
        for pattern in self.explanation_patterns:
            if re.search(pattern, user_input_lower):
                return TaskType.EXPLANATION

        # Check for coding patterns
        for pattern in self.coding_patterns:
            if re.search(pattern, user_input_lower):
                return TaskType.CODING

        # Default to general
        return TaskType.GENERAL

    def parse_provider_and_model(self, provider_str: str | None, model_str: str | None) -> tuple[Provider, str]:
        """Parse provider and model from CLI arguments."""
        provider = Provider.ANTHROPIC  # default
        if provider_str:
            try:
                provider = Provider(provider_str.lower())
            except ValueError:
                pass  # Use default

        # Default models per provider
        model_defaults = {
            Provider.ANTHROPIC: "claude-3-5-sonnet-20241022",
            Provider.OPENAI: "gpt-4",
            Provider.GOOGLE: "gemini-pro",
        }

        model = model_str or model_defaults[provider]
        return provider, model

    def create_request(
        self,
        user_input: str,
        provider_str: str | None = None,
        model_str: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> LLMRequest:
        """Create an LLM request from user input."""
        task_type = self.detect_task_type(user_input)
        provider, model = self.parse_provider_and_model(provider_str, model_str)

        return LLMRequest(
            task_type=task_type,
            user_input=user_input,
            context=context,
            provider=provider,
            model=model,
        )