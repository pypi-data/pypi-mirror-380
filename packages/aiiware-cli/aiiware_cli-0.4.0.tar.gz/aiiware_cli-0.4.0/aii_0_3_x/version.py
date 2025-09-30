"""Version management for aii package."""

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

from typing import Any


def _load_version() -> str:
    """Load version from package metadata.

    This works for both development installs (pip install -e .)
    and PyPI installs (uv tool install aiiware-cli).
    """
    metadata_modules: list[Any] = []

    try:
        from importlib import metadata as stdlib_metadata

        metadata_modules.append(stdlib_metadata)
    except ImportError:  # pragma: no cover - Python <3.8 fallback
        pass

    try:
        import importlib_metadata as backport_metadata

        metadata_modules.append(backport_metadata)
    except ImportError:  # pragma: no cover - dependency unavailable
        pass

    for module in metadata_modules:
        try:
            return str(module.version("aiiware-cli"))
        except Exception:
            continue

    return "0.3.0"  # Fallback version


def _load_description() -> str:
    """Load description from package metadata."""
    metadata_modules: list[Any] = []

    try:
        from importlib import metadata as stdlib_metadata

        metadata_modules.append(stdlib_metadata)
    except ImportError:  # pragma: no cover - Python <3.8 fallback
        pass

    try:
        import importlib_metadata as backport_metadata

        metadata_modules.append(backport_metadata)
    except ImportError:  # pragma: no cover - dependency unavailable
        pass

    for module in metadata_modules:
        try:
            metadata = module.metadata("aiiware-cli")
            return str(metadata.get("Summary", ""))
        except Exception:
            continue

    return "aii — AI × Intelligence companion for translate, code, write, explain & automate."  # Fallback description


__version__ = _load_version()
__description__ = _load_description()
