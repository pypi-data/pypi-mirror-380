"""Main CLI interface for aii-mvp."""

import asyncio
import os
import sys
from typing import Any

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from ..commands.processor import CommandProcessor
from ..providers.llm import LLMService


console = Console()


def validate_environment() -> list[str]:
    """Validate that required API keys are available."""
    missing_keys = []

    if not os.getenv("ANTHROPIC_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        missing_keys.append("At least one API key (ANTHROPIC_API_KEY or OPENAI_API_KEY) is required")

    return missing_keys


@click.command()
@click.argument("query", nargs=-1, required=False)
@click.option("-p", "--provider", help="LLM provider (anthropic, openai)")
@click.option("--model", help="Specific model to use")
@click.option("-v", "--verbose", is_flag=True, help="Verbose output")
@click.version_option(version="0.1.0")
def main(query: tuple[str, ...], provider: str | None, model: str | None, verbose: bool) -> None:
    """aii-mvp: Modern LLM-powered CLI Assistant.

    A clean, focused implementation of an LLM-powered command-line interface.

    Examples:
        aii-mvp translate hello to spanish
        aii-mvp explain quantum computing
        aii-mvp write a Python function to sort a list
        aii-mvp -p openai --model gpt-4 translate hello to japanese
    """
    if not query:
        console.print(Panel(
            Text("aii-mvp: Modern LLM-powered CLI Assistant\\n\\n"
                 "Try: aii-mvp translate hello to spanish", style="blue"),
            title="Welcome"
        ))
        return

    # Validate environment
    missing_keys = validate_environment()
    if missing_keys:
        console.print(Panel(
            "\\n".join(missing_keys) + "\\n\\nPlease set up your API keys in environment variables.",
            title="❌ Configuration Error",
            style="red"
        ))
        sys.exit(1)

    # Join query parts
    user_input = " ".join(query)

    # Run async main
    asyncio.run(async_main(user_input, provider, model, verbose))


async def async_main(user_input: str, provider: str | None, model: str | None, verbose: bool) -> None:
    """Async main function."""
    try:
        # Initialize services
        processor = CommandProcessor()
        llm_service = LLMService()

        # Check provider availability
        available_providers = llm_service.get_available_providers()
        if not available_providers:
            console.print(Panel(
                "No LLM providers available. Please check your API keys.",
                title="❌ Provider Error",
                style="red"
            ))
            return

        if verbose:
            console.print(f"Available providers: {[p.value for p in available_providers]}")

        # Create request
        request = processor.create_request(user_input, provider, model)

        # Validate provider availability
        if request.provider not in available_providers:
            console.print(Panel(
                f"Provider {request.provider.value} not available. Using {available_providers[0].value}.",
                style="yellow"
            ))
            request.provider = available_providers[0]

        if verbose:
            console.print(f"Task type detected: {request.task_type.value}")
            console.print(f"Using provider: {request.provider.value}")
            console.print(f"Using model: {request.model}")

        # Show processing indicator
        with console.status(f"Processing with {request.provider.value}..."):
            response = await llm_service.process_request(request)

        # Display response
        console.print(Panel(
            response.content,
            title=f"✨ Response ({response.provider_used})",
            style="green"
        ))

        if verbose and response.reasoning:
            console.print(Panel(
                response.reasoning,
                title="🤔 Reasoning",
                style="blue"
            ))

    except Exception as e:
        console.print(Panel(
            f"Error: {e}",
            title="❌ Error",
            style="red"
        ))
        sys.exit(1)


if __name__ == "__main__":
    main()