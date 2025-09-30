#!/usr/bin/env python3
"""
Simple aiia entry point that works around import conflicts
"""

def main():
    """Entry point that handles import resolution correctly."""
    import sys
    import os
    import importlib.util
    import asyncio

    try:
        # Get the directory where this script is located (should be in aii package)
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the standalone aiia script from the same directory
        standalone_path = os.path.join(script_dir, "aiia_standalone_final.py")
        if os.path.exists(standalone_path):
            spec = importlib.util.spec_from_file_location("aiia_standalone", standalone_path)
            aiia_module = importlib.util.module_from_spec(spec)

            # Modify the module to use the correct aii path
            # The aii modules should be available from the parent directory
            aii_parent = os.path.dirname(script_dir)  # Go up from aii package to its parent
            if aii_parent not in sys.path:
                sys.path.insert(0, aii_parent)

            # Execute the module
            spec.loader.exec_module(aiia_module)

            # Run the standalone main function
            return asyncio.run(aiia_module.main())
        else:
            print("❌ Error: aiia_standalone_final.py not found at", standalone_path, file=sys.stderr)
            return 1

    except Exception as e:
        print(f"❌ Error running aiia: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())