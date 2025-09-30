"""Status Display - Loading animations and progress feedback"""

import sys
import threading
import time
from typing import Any


class StatusDisplay:
    """Manages loading animations and status messages"""

    def __init__(self, use_emojis: bool = True, use_animations: bool = True):
        self.use_emojis = use_emojis
        self.use_animations = use_animations
        self.is_displaying = False
        self._display_thread = None
        self._stop_event = threading.Event()

        # Animation frames
        self.spinner_frames = (
            ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            if use_emojis
            else ["|", "/", "-", "\\"]
        )
        self.dots_frames = (
            ["⠋", "⠙", "⠚", "⠞", "⠖", "⠦", "⠴", "⠲", "⠳", "⠓"]
            if use_emojis
            else [".", "..", "...", "...."]
        )

    def start_loading(self, message: str, animation_type: str = "spinner") -> None:
        """Start displaying loading animation with message"""
        if self.is_displaying:
            self.stop_loading()

        # If animations are disabled, just print the message once
        if not self.use_animations:
            print(f"[LOADING] {message}")
            return

        self.is_displaying = True
        self._stop_event.clear()

        # Choose animation frames
        frames = (
            self.spinner_frames if animation_type == "spinner" else self.dots_frames
        )

        self._display_thread = threading.Thread(
            target=self._animate, args=(message, frames), daemon=True
        )
        self._display_thread.start()

    def _animate(self, message: str, frames: list[str]) -> None:
        """Display animation frames"""
        frame_index = 0

        while not self._stop_event.is_set():
            # Clear current line and show animation
            sys.stdout.write(f"\r{frames[frame_index]} {message}")
            sys.stdout.flush()

            frame_index = (frame_index + 1) % len(frames)
            time.sleep(0.1)  # 100ms per frame

    def update_message(self, new_message: str) -> None:
        """Update the loading message (for future enhancement)"""
        # This would require more complex thread communication
        # For now, we'll restart with new message
        if self.is_displaying:
            self.stop_loading()
            self.start_loading(new_message)

    def stop_loading(self) -> None:
        """Stop loading animation and clear the line"""
        # If animations are disabled, there's nothing to stop
        if not self.use_animations:
            return

        if self.is_displaying and self._display_thread:
            self._stop_event.set()
            self._display_thread.join(timeout=0.5)

            # Clear the loading line
            sys.stdout.write(
                "\r" + " " * 80 + "\r"
            )  # Clear with spaces, then return to start
            sys.stdout.flush()

            self.is_displaying = False
            self._display_thread = None

    def show_status(self, message: str, status_type: str = "info") -> None:
        """Show a status message without animation"""
        icons = {
            "info": "ℹ️" if self.use_emojis else "[INFO]",
            "working": "⚙️" if self.use_emojis else "[WORK]",
            "thinking": "🧠" if self.use_emojis else "[THINK]",
            "gathering": "📊" if self.use_emojis else "[GATHER]",
            "generating": "✨" if self.use_emojis else "[GEN]",
            "success": "✅" if self.use_emojis else "[OK]",
            "error": "❌" if self.use_emojis else "[ERR]",
        }

        icon = icons.get(status_type, icons["info"])
        print(f"{icon} {message}")

    async def async_status_context(
        self, message: str, animation_type: str = "spinner"
    ) -> "AsyncStatusContext":
        """Async context manager for loading states"""
        return AsyncStatusContext(self, message, animation_type)


class AsyncStatusContext:
    """Async context manager for loading animations"""

    def __init__(
        self, status_display: StatusDisplay, message: str, animation_type: str
    ):
        self.status_display = status_display
        self.message = message
        self.animation_type = animation_type

    async def __aenter__(self) -> "AsyncStatusContext":
        self.status_display.start_loading(self.message, self.animation_type)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        self.status_display.stop_loading()


class ProgressTracker:
    """Tracks and displays progress for multi-step operations"""

    def __init__(self, use_emojis: bool = True):
        self.use_emojis = use_emojis
        self.steps = []
        self.current_step = 0

    def add_step(self, description: str) -> None:
        """Add a step to track"""
        self.steps.append(
            {
                "description": description,
                "status": "pending",  # pending, in_progress, completed, failed
                "start_time": None,
                "end_time": None,
            }
        )

    def start_step(self, step_index: int | None = None) -> None:
        """Start a specific step (or next step if none specified)"""
        if step_index is None:
            step_index = self.current_step

        if 0 <= step_index < len(self.steps):
            self.steps[step_index]["status"] = "in_progress"
            self.steps[step_index]["start_time"] = time.time()
            self.current_step = step_index
            self._display_progress()

    def complete_step(
        self, step_index: int | None = None, success: bool = True
    ) -> None:
        """Complete a specific step"""
        if step_index is None:
            step_index = self.current_step

        if 0 <= step_index < len(self.steps):
            self.steps[step_index]["status"] = "completed" if success else "failed"
            self.steps[step_index]["end_time"] = time.time()

            if success and step_index == self.current_step:
                self.current_step += 1

            self._display_progress()

    def _display_progress(self) -> None:
        """Display current progress"""
        status_icons = {
            "pending": "⏳" if self.use_emojis else "[ ]",
            "in_progress": "⚙️" if self.use_emojis else "[.]",
            "completed": "✅" if self.use_emojis else "[✓]",
            "failed": "❌" if self.use_emojis else "[✗]",
        }

        print("\n📊 Progress:" if self.use_emojis else "\n[PROGRESS]")
        for step in self.steps:
            icon = status_icons[step["status"]]
            print(f"  {icon} {step['description']}")

    def get_summary(self) -> dict[str, Any]:
        """Get progress summary"""
        completed = sum(1 for step in self.steps if step["status"] == "completed")
        failed = sum(1 for step in self.steps if step["status"] == "failed")
        total = len(self.steps)

        return {
            "total_steps": total,
            "completed": completed,
            "failed": failed,
            "in_progress": sum(
                1 for step in self.steps if step["status"] == "in_progress"
            ),
            "pending": total - completed - failed,
            "success_rate": completed / total if total > 0 else 0,
        }
