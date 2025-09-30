#!/usr/bin/env python3
"""
Standalone aiia CLI

This is a complete, standalone implementation of the aiia v2 CLI that doesn't
rely on complex package imports and demonstrates the full v2 functionality.
"""

import sys
import asyncio
import argparse
from pathlib import Path
import importlib.util
import os

def load_module_from_path(module_name, file_path):
    """Load a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def setup_imports():
    """Setup imports by adding the aii directory to the path."""
    current_dir = Path(__file__).parent

    # When installed as package, we're already in the aii directory
    # So current_dir IS the aii directory, we just need to add its parent to path
    parent_dir = current_dir.parent
    if parent_dir not in [Path(p) for p in sys.path]:
        sys.path.insert(0, str(parent_dir))

    # Also try the current directory itself
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))

    return True

async def run_aiia_command(user_input: str, verbose: bool = False):
    """Run an aiia command using the v2 architecture."""

    if not setup_imports():
        print("❌ Error: Could not find aii directory", file=sys.stderr)
        return False

    try:
        # Import the required modules
        from commands.loader import load_command_catalog
        from commands.routing import CommandRouter
        from commands.handlers.system import HelpHandler, VersionHandler, StatusHandler
        from commands.handlers.translate import TranslateHandler, DetectLanguageHandler, QuickTranslateHandler
        from commands.executor import ExecutionResult, ExecutionContext, CommandHandler
        from commands.schema import CommandModel

        # Create simple executor
        handlers = {
            'aii.commands.handlers.system.HelpHandler': HelpHandler(),
            'aii.commands.handlers.system.VersionHandler': VersionHandler(),
            'aii.commands.handlers.system.StatusHandler': StatusHandler(),
            'aii.commands.handlers.translate.TranslateHandler': TranslateHandler(),
            'aii.commands.handlers.translate.DetectLanguageHandler': DetectLanguageHandler(),
            'aii.commands.handlers.translate.QuickTranslateHandler': QuickTranslateHandler(),
        }

        if verbose:
            print(f"🔧 Processing: {user_input}")

        # Load patterns and create router
        patterns_dir = Path(__file__).parent / "patterns"
        catalog = load_command_catalog(str(patterns_dir))
        router = CommandRouter(catalog)

        # Route command
        routes = router.route(user_input, max_matches=1)

        if not routes:
            print(f"❌ No command found for input: '{user_input}'")
            print("💡 Try: python aiia_standalone_final.py help")
            return False

        route = routes[0]
        command = route.command

        if verbose:
            print(f"🎯 Routed to: {command.name} (confidence: {route.confidence:.2f})")

        # Extract parameters
        parameters = {}
        if route.groups and command.parameters:
            for i, group_value in enumerate(route.groups):
                if i < len(command.parameters) and group_value is not None:
                    param_name = command.parameters[i].name
                    parameters[param_name] = group_value

        # Get handler
        handler_key = command.handler
        if handler_key not in handlers:
            print(f"❌ Handler not found: {handler_key}")
            return False

        handler = handlers[handler_key]

        # Create context and execute
        context = ExecutionContext(
            command=command,
            parameters=parameters,
            session_id="standalone_session",
            user_id="standalone_user"
        )

        result = await handler.execute(command, context)

        # Output result
        if result.success:
            print(result.output)
            return True
        else:
            print(f"❌ Command failed: {result.error}", file=sys.stderr)
            return False

    except Exception as e:
        print(f"❌ Error executing command: {e}", file=sys.stderr)
        if verbose:
            import traceback
            traceback.print_exc()
        return False

def create_parser():
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        prog="aiia",
        description="aii v2 Alpha - Your AI-powered CLI assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python aiia_standalone_final.py help
  python aiia_standalone_final.py version
  python aiia_standalone_final.py status
  python aiia_standalone_final.py translate "Hello" to Spanish
  python aiia_standalone_final.py detect "Hola mundo"

This standalone version demonstrates the full aii v2 architecture.
        """
    )

    parser.add_argument(
        "command",
        nargs="*",
        help="Command to execute"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    return parser

async def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        print("\n💡 Try: python aiia_standalone_final.py help")
        return 0

    user_input = " ".join(args.command)

    print("🚀 aii v2 Alpha (aiia) - Standalone CLI")
    if args.verbose:
        print(f"📦 Architecture: v2.0.0-alpha")
        print(f"🎯 Input: {user_input}")
        print()

    success = await run_aiia_command(user_input, verbose=args.verbose)

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))