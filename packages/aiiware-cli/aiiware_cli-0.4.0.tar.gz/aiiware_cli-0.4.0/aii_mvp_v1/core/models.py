"""Core data models for the MVP CLI."""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class TaskType(Enum):
    """Types of tasks the CLI can handle."""
    TRANSLATION = "translation"
    EXPLANATION = "explanation"
    CODING = "coding"
    SHELL = "shell"
    GENERAL = "general"


class Provider(Enum):
    """LLM providers."""
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GOOGLE = "google"


@dataclass
class LLMRequest:
    """Request to an LLM provider."""
    task_type: TaskType
    user_input: str
    context: dict[str, Any] | None = None
    provider: Provider = Provider.ANTHROPIC
    model: str = "claude-3-5-sonnet-20241022"


@dataclass
class LLMResponse:
    """Response from an LLM provider."""
    content: str
    reasoning: str | None = None
    model_used: str | None = None
    provider_used: str | None = None