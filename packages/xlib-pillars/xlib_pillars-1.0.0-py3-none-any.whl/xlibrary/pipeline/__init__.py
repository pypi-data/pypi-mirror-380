"""
xlibrary.pipeline - Universal pipeline management system

This module provides a comprehensive pipeline management system for tracking
items through multi-stage workflows with full state persistence and recovery.

Core Features:
- Universal pipeline state management
- Configurable multi-stage workflows
- Full state persistence with JSON index
- Error handling and recovery capabilities
- Progress tracking and statistics
- Stage-specific processing logic
- Rollback and retry mechanisms

The system is completely agnostic to use case and can be used for any process
that moves items through defined stages.

Usage Examples:
    from xlibrary.pipeline import PipelineManager, PipelineStage

    # Define stages
    stages = [
        PipelineStage("download", "Download files"),
        PipelineStage("process", "Process content"),
        PipelineStage("upload", "Upload results")
    ]

    # Initialize manager
    manager = PipelineManager("pipeline.json", stages)

    # Add items to pipeline
    item_id = manager.add_item("/path/to/file", metadata={"priority": "high"})

    # Process through stages
    manager.process_stage("download", item_id)
    manager.process_stage("process", item_id)
    manager.process_stage("upload", item_id)
"""

from .core.manager import PipelineManager, PipelineError
from .core.types import (
    PipelineItem,
    PipelineStage,
    StageResult,
    ItemStatus,
    StageStatus,
    PipelineStatistics
)

__version__ = "1.0.0"
__all__ = [
    # Main class
    "PipelineManager",

    # Data types
    "PipelineItem",
    "PipelineStage",
    "StageResult",
    "PipelineStatistics",

    # Enums
    "ItemStatus",
    "StageStatus",

    # Exceptions
    "PipelineError"
]