"""Function Plugin Layer - Universal function system with context gathering"""

from ..core.registry.function_registry import FunctionRegistry
from .analysis.analysis_functions import (
    ExplainFunction,
    ResearchFunction,
    SummarizeFunction,
)
from .code.code_functions import CodeGenerateFunction, CodeReviewFunction
from .content.content_functions import (
    ContentGenerateFunction,
    EmailContentFunction,
    SocialPostFunction,
    TwitterContentFunction,
    UniversalContentFunction,
)
from .context.context_functions import (
    FileContextFunction,
    GitContextFunction,
    SystemContextFunction,
)
from .git.git_functions import GitCommitFunction, GitDiffFunction, GitStatusFunction
from .shell.contextual_shell_functions import (
    ContextualShellFunction,
)
from .shell.enhanced_shell_functions import (
    EnhancedShellCommandFunction,
)
from .shell.shell_functions import (
    FindCommandFunction,
    ShellCommandFunction,
)
from .shell.streaming_shell_functions import (
    StreamingShellFunction,
)
from .translation.translation_functions import TranslationFunction


def register_all_functions(registry: FunctionRegistry) -> None:
    """Register all built-in functions with the registry"""

    # Context functions (fundamental)
    registry.register_plugin(GitContextFunction())
    registry.register_plugin(FileContextFunction())
    registry.register_plugin(SystemContextFunction())

    # Content generation functions (universal)
    registry.register_plugin(UniversalContentFunction())
    registry.register_plugin(TwitterContentFunction())
    registry.register_plugin(EmailContentFunction())
    registry.register_plugin(ContentGenerateFunction())
    registry.register_plugin(SocialPostFunction())

    # Git functions
    registry.register_plugin(GitCommitFunction())
    registry.register_plugin(GitDiffFunction())
    registry.register_plugin(GitStatusFunction())

    # Translation functions
    registry.register_plugin(TranslationFunction())

    # Code functions
    registry.register_plugin(CodeReviewFunction())
    registry.register_plugin(CodeGenerateFunction())

    # Analysis functions
    registry.register_plugin(SummarizeFunction())
    registry.register_plugin(ExplainFunction())
    registry.register_plugin(ResearchFunction())

    # Shell functions with Smart Command Triage System
    registry.register_plugin(EnhancedShellCommandFunction())
    registry.register_plugin(FindCommandFunction())

    # Streaming shell functions with real-time feedback
    registry.register_plugin(StreamingShellFunction())

    # Contextual shell functions with conversation memory
    registry.register_plugin(ContextualShellFunction())

    # Function registration complete - no output needed for clean UX


__all__ = [
    "GitCommitFunction",
    "GitDiffFunction",
    "GitStatusFunction",
    "TranslationFunction",
    "CodeGenerateFunction",
    "CodeReviewFunction",
    "SummarizeFunction",
    "ExplainFunction",
    "ResearchFunction",
    "GitContextFunction",
    "FileContextFunction",
    "SystemContextFunction",
    "UniversalContentFunction",
    "TwitterContentFunction",
    "EmailContentFunction",
    "ContentGenerateFunction",
    "SocialPostFunction",
    "ShellCommandFunction",
    "FindCommandFunction",
    "EnhancedShellCommandFunction",
    "StreamingShellFunction",
    "ContextualShellFunction",
    "register_all_functions",
]
