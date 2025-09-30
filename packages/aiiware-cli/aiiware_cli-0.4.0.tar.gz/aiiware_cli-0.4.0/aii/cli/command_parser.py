"""Command Parser - Parse CLI commands and arguments"""

import argparse
import sys
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ParsedCommand:
    """Represents a parsed CLI command"""

    command: str | None = None
    args: dict[str, Any] = field(default_factory=dict)
    input_text: str = ""
    continue_chat: str | None = None
    new_chat: bool = False
    offline: bool = False
    interactive: bool = False


class CommandParser:
    """Main command parser for AII CLI"""

    def __init__(self) -> None:
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the main argument parser"""
        parser = argparse.ArgumentParser(
            prog="aii",
            description="AII - LLM-powered CLI assistant with intelligent intent recognition",
        )

        # Version option
        parser.add_argument(
            "--version", action="version", version="aiiware-cli 0.4.0"
        )

        # Global options
        parser.add_argument(
            "--continue-chat", "-c", type=str, help="Continue specific chat by ID"
        )

        parser.add_argument(
            "--new-chat", "-n", action="store_true", help="Force new chat session"
        )

        parser.add_argument(
            "--offline",
            action="store_true",
            help="Run in offline mode (no web/MCP access)",
        )

        parser.add_argument(
            "--config",
            type=str,
            default="~/.config/aii/config.yaml",
            help="Configuration file path",
        )

        # Verbosity options (mutually exclusive)
        verbosity_group = parser.add_mutually_exclusive_group()
        verbosity_group.add_argument(
            "--minimal", "-m", action="store_true",
            help="Minimal output (no timing, tokens, or semantic analysis)"
        )
        verbosity_group.add_argument(
            "--verbose", "-v", action="store_true",
            help="Verbose output (detailed metrics and analysis)"
        )
        verbosity_group.add_argument(
            "--debug", "-d", action="store_true",
            help="Debug output (all metrics, trace info, and performance data)"
        )

        # Output customization options
        parser.add_argument(
            "--no-colors", action="store_true",
            help="Disable colored output"
        )
        parser.add_argument(
            "--no-emojis", action="store_true",
            help="Disable emoji icons"
        )
        parser.add_argument(
            "--no-animations", action="store_true",
            help="Disable loading animations"
        )
        parser.add_argument(
            "--show-tokens", action="store_true",
            help="Always show token usage"
        )
        parser.add_argument(
            "--show-confidence", action="store_true",
            help="Always show confidence scores"
        )
        parser.add_argument(
            "--show-cost", action="store_true",
            help="Show cost estimates"
        )

        parser.add_argument(
            "--interactive", "-i", action="store_true", help="Enter interactive mode"
        )

        # Subcommands - these will consume all remaining args when matched
        subparsers = parser.add_subparsers(
            dest="command", help="Available commands", required=False
        )

        # Chat history management
        self._add_history_commands(subparsers)

        # Configuration commands
        self._add_config_commands(subparsers)

        # Interactive mode
        chat_parser = subparsers.add_parser("chat", help="Enter interactive chat mode")
        chat_parser.add_argument(
            "--continue-chat", "-c", type=str, help="Continue specific chat"
        )

        return parser

    def _add_history_commands(self, subparsers: Any) -> None:
        """Add chat history management commands"""
        history_parser = subparsers.add_parser(
            "history", help="Chat history management"
        )
        history_subparsers = history_parser.add_subparsers(
            dest="history_action", required=False
        )

        # List chats
        list_parser = history_subparsers.add_parser("list", help="List chat history")
        list_parser.add_argument(
            "--detailed", action="store_true", help="Show detailed info"
        )
        list_parser.add_argument("--since", type=str, help="Show chats since date/time")
        list_parser.add_argument(
            "--from", dest="from_date", type=str, help="Start date"
        )
        list_parser.add_argument("--to", dest="to_date", type=str, help="End date")

        # Search chats
        search_parser = history_subparsers.add_parser(
            "search", help="Search chat history"
        )
        search_parser.add_argument("query", help="Search query")
        search_parser.add_argument("--tag", type=str, help="Filter by tag")
        search_parser.add_argument(
            "--content", action="store_true", help="Search in content"
        )

        # Continue chat
        continue_parser = history_subparsers.add_parser(
            "continue", help="Continue chat"
        )
        continue_parser.add_argument("chat_id", help="Chat ID to continue")
        continue_parser.add_argument(
            "--context-limit", type=int, default=20, help="Number of messages to load"
        )

        # Export/Import
        export_parser = history_subparsers.add_parser("export", help="Export chat")
        export_parser.add_argument("chat_id", nargs="?", help="Chat ID to export")
        export_parser.add_argument(
            "--format",
            choices=["json", "markdown"],
            default="json",
            help="Export format",
        )
        export_parser.add_argument(
            "--all", action="store_true", help="Export all chats"
        )
        export_parser.add_argument("--since", type=str, help="Export since date")

        import_parser = history_subparsers.add_parser("import", help="Import chat")
        import_parser.add_argument("file_path", help="File to import")

        # Management operations
        rename_parser = history_subparsers.add_parser("rename", help="Rename chat")
        rename_parser.add_argument("chat_id", help="Chat ID")
        rename_parser.add_argument("new_name", help="New chat name")

        tag_parser = history_subparsers.add_parser("tag", help="Tag chat")
        tag_parser.add_argument("chat_id", help="Chat ID")
        tag_parser.add_argument("tags", nargs="+", help="Tags to add")

        archive_parser = history_subparsers.add_parser("archive", help="Archive chat")
        archive_parser.add_argument("chat_id", help="Chat ID")

        delete_parser = history_subparsers.add_parser("delete", help="Delete chat")
        delete_parser.add_argument("chat_id", help="Chat ID")
        delete_parser.add_argument(
            "--confirm", action="store_true", required=True, help="Confirm deletion"
        )

    def _add_config_commands(self, subparsers: Any) -> None:
        """Add configuration management commands"""
        config_parser = subparsers.add_parser("config", help="Configuration management")
        config_subparsers = config_parser.add_subparsers(
            dest="config_action", required=False
        )

        # Initialize config
        config_subparsers.add_parser("init", help="Initialize configuration")

        # Show config
        show_parser = config_subparsers.add_parser("show", help="Show configuration")
        show_parser.add_argument("--section", type=str, help="Show specific section")

        # Set config values
        set_parser = config_subparsers.add_parser("set", help="Set configuration value")
        set_parser.add_argument("key", help="Configuration key")
        set_parser.add_argument("value", help="Configuration value")

        # API key management
        key_parser = config_subparsers.add_parser("key", help="API key management")
        key_subparsers = key_parser.add_subparsers(dest="key_action", required=False)

        set_key_parser = key_subparsers.add_parser("set", help="Set API key")
        set_key_parser.add_argument(
            "provider", help="Provider name (openai, anthropic, etc.)"
        )

        # List configured providers parser
        key_subparsers.add_parser("list", help="List configured providers")

        # OAuth login/logout commands
        oauth_parser = config_subparsers.add_parser("oauth", help="OAuth authentication")
        oauth_subparsers = oauth_parser.add_subparsers(dest="oauth_action", required=False)

        # Login command
        oauth_subparsers.add_parser("login", help="Login with subscription account")

        # Logout command
        oauth_subparsers.add_parser("logout", help="Logout and clear credentials")

        # Status command
        oauth_subparsers.add_parser("status", help="Show authentication status")

    def parse_args(self, args: list[str] | None = None) -> ParsedCommand:
        """Parse command line arguments"""
        if args is None:
            args = sys.argv[1:]

        # Check for --version or --help flag first (should be handled by argparse and exit)
        if "--version" in args or "--help" in args or "-h" in args:
            # Let argparse handle --version, --help and exit
            self.parser.parse_args(args)
            # This should never be reached because argparse exits after these flags
            raise SystemExit(0)

        # Check if this looks like a structured command first
        if args and args[0] in ["history", "config", "chat"]:
            # Try parsing as structured command
            try:
                parsed = self.parser.parse_args(args)
                return ParsedCommand(
                    command=parsed.command,
                    args=vars(parsed),
                    input_text="",
                    continue_chat=getattr(parsed, "continue_chat", None),
                    new_chat=getattr(parsed, "new_chat", False),
                    offline=getattr(parsed, "offline", False),
                    interactive=getattr(parsed, "interactive", False)
                    or parsed.command == "chat",
                )
            except SystemExit:
                # If structured parsing failed, fall through to free-form
                pass

        # Treat as free-form input - parse global options manually
        filtered_input_args = []
        extracted_options = {
            "continue_chat": None,
            "new_chat": False,
            "offline": False,
            "config": "~/.config/aii/config.yaml",
            "verbose": False,
            "minimal": False,
            "debug": False,
            "interactive": False,
            "no_colors": False,
            "no_emojis": False,
            "no_animations": False,
            "show_tokens": False,
            "show_confidence": False,
            "show_cost": False,
        }

        i = 0
        while i < len(args):
            arg = args[i]
            if arg == "--continue-chat" or arg == "-c":
                if i + 1 < len(args):
                    extracted_options["continue_chat"] = args[i + 1]
                    i += 2
                else:
                    i += 1
            elif arg == "--new-chat" or arg == "-n":
                extracted_options["new_chat"] = True
                i += 1
            elif arg == "--offline":
                extracted_options["offline"] = True
                i += 1
            elif arg == "--verbose" or arg == "-v":
                extracted_options["verbose"] = True
                i += 1
            elif arg == "--minimal" or arg == "-m":
                extracted_options["minimal"] = True
                i += 1
            elif arg == "--debug" or arg == "-d":
                extracted_options["debug"] = True
                i += 1
            elif arg == "--no-colors":
                extracted_options["no_colors"] = True
                i += 1
            elif arg == "--no-emojis":
                extracted_options["no_emojis"] = True
                i += 1
            elif arg == "--no-animations":
                extracted_options["no_animations"] = True
                i += 1
            elif arg == "--show-tokens":
                extracted_options["show_tokens"] = True
                i += 1
            elif arg == "--show-confidence":
                extracted_options["show_confidence"] = True
                i += 1
            elif arg == "--show-cost":
                extracted_options["show_cost"] = True
                i += 1
            elif arg == "--interactive" or arg == "-i":
                extracted_options["interactive"] = True
                i += 1
            elif arg == "--config":
                if i + 1 < len(args):
                    extracted_options["config"] = args[i + 1]
                    i += 2
                else:
                    i += 1
            elif arg.startswith("--config="):
                extracted_options["config"] = arg.split("=", 1)[1]
                i += 1
            else:
                filtered_input_args.append(arg)
                i += 1

        input_text = " ".join(filtered_input_args) if filtered_input_args else None
        interactive = extracted_options["interactive"] or (
            not input_text and not extracted_options["continue_chat"]
        )

        return ParsedCommand(
            command="main",
            args={**extracted_options, "command": None},
            input_text=input_text or "",
            continue_chat=(
                extracted_options["continue_chat"]
                if isinstance(extracted_options["continue_chat"], str)
                else None
            ),
            new_chat=bool(extracted_options["new_chat"]),
            offline=bool(extracted_options["offline"]),
            interactive=bool(interactive),
        )

    def print_help(self) -> None:
        """Print help message"""
        self.parser.print_help()
