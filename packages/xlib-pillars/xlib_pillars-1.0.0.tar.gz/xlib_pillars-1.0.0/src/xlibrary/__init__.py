"""
xlibrary - A comprehensive library ecosystem with modular pillars

Available pillars:
- ai: AI provider abstraction (Claude, OpenAI, DeepSeek)
- config: Configuration management with TOML support
- download: Advanced download manager with multi-content support
- encryption: Security and encryption utilities
- media: Advanced media processing (video, image, watermarking)
- cli: Professional command-line interface framework

Installation:
- pip install xlibrary[ai]         # AI pillar only
- pip install xlibrary[config]     # Config pillar only
- pip install xlibrary[download]   # Download pillar only
- pip install xlibrary[media]      # Media pillar only
- pip install xlibrary[cli]        # CLI pillar only
- pip install xlibrary[all]        # All pillars
"""

__version__ = "1.0.0"
__author__ = "xlibrary"
__email__ = "contact@xlibrary.dev"

def get_version():
    """Get xlibrary version."""
    return __version__

def get_pillars():
    """Get available pillars in this installation."""
    pillars = []

    # Check each pillar availability
    try:
        from . import ai
        pillars.append("ai")
    except ImportError:
        pass

    try:
        from . import config
        pillars.append("config")
    except ImportError:
        pass

    try:
        from . import download
        pillars.append("download")
    except ImportError:
        pass

    try:
        from . import encryption
        pillars.append("encryption")
    except ImportError:
        pass

    try:
        from . import media
        pillars.append("media")
    except ImportError:
        pass

    try:
        from . import cli
        pillars.append("cli")
    except ImportError:
        pass

    return pillars

# Core functions always available
__all__ = [
    "get_version",
    "get_pillars"
]

# Try to import AI pillar components for backward compatibility
try:
    from .ai import AIManager, AIResponse, AIConfig
    __all__.extend(["AIManager", "AIResponse", "AIConfig"])
except ImportError:
    # AI pillar not installed
    pass