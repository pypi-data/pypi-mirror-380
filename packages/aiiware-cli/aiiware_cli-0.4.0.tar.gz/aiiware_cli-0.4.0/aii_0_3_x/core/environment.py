"""Environment detection for AII."""

# Copyright 2025-present aiiware.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import os
import platform
from pathlib import Path
from typing import Protocol

from .models import OSType, ShellType


class EnvironmentDetector(Protocol):
    """Protocol for environment detection strategies."""

    def detect_os(self) -> OSType:
        """Detect the operating system."""
        ...

    def detect_shell(self) -> ShellType:
        """Detect the current shell."""
        ...


class SystemEnvironmentDetector:
    """Concrete implementation of environment detection."""

    def detect_os(self) -> OSType:
        """Detect operating system using platform module."""
        system = platform.system().lower()
        if system == "darwin":
            return OSType.MACOS
        elif system == "linux":
            return OSType.LINUX
        return OSType.UNKNOWN

    def detect_shell(self) -> ShellType:
        """Detect current shell using multiple strategies."""
        # Strategy 1: Fish-specific environment variable
        if os.environ.get("FISH_VERSION"):
            return ShellType.FISH

        # Strategy 2: Check parent process
        try:
            import psutil

            current = psutil.Process()
            parent = current.parent()
            if parent:
                parent_name = parent.name().lower()
                for shell_type in ShellType:
                    if shell_type.value in parent_name:
                        return shell_type
        except Exception:
            pass

        # Strategy 3: SHELL environment variable
        shell_path = os.environ.get("SHELL", "")
        if shell_path:
            shell_name = Path(shell_path).name
            try:
                return ShellType(shell_name)
            except ValueError:
                pass

        # Default fallback
        return ShellType.FISH
