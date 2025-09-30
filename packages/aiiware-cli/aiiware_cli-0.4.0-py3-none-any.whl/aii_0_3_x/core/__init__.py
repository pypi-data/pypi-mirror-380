"""Core models and utilities for AII."""

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

from .environment import EnvironmentDetector, SystemEnvironmentDetector
from .exceptions import GitCommandError
from .models import (
    AIMode,
    AIRequest,
    AIResponse,
    ConversationHistory,
    ConversationMessage,
    EnvironmentContext,
    OSType,
    ProviderType,
    ShellType,
)
from .utils import debug_print

__all__ = [
    # Enums
    "AIMode",
    "OSType",
    "ShellType",
    "ProviderType",
    # Data classes
    "EnvironmentContext",
    "AIRequest",
    "AIResponse",
    "ConversationMessage",
    "ConversationHistory",
    # Environment detection
    "EnvironmentDetector",
    "SystemEnvironmentDetector",
    # Exceptions
    "GitCommandError",
    # Utilities
    "debug_print",
]
