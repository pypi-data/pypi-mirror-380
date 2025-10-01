"""
XLibrary Pipeline Management

Universal pipeline state management system for tracking items through
multi-stage workflows. Agnostic to use case - works for any process
that moves items through defined stages.

Features:
- JSON-based state persistence
- Rich metadata tracking per stage
- Error handling and recovery
- Progress reporting and analytics
- Hash-based file verification
- Resumable workflows

Usage:
    from xlibrary.pipeline import PipelineManager
    
    # Define your workflow stages
    pipeline = PipelineManager(
        index_file="my_workflow.json",
        stages=["input", "processing", "analysis", "output"]
    )
    
    # Track items through stages
    item_id = pipeline.add_item("document_001", source_file="uploads/doc.pdf")
    pipeline.update_stage(item_id, "processing", metadata={"pages": 12})
    pipeline.update_stage(item_id, "analysis", output_file="results/analysis.txt")
    
    # Monitor and report
    stats = pipeline.get_statistics()
    incomplete = pipeline.get_items_by_status("in_progress")
"""

from .manager import PipelineManager, PipelineError
from .types import PipelineStage, ItemStatus, PipelineItem

__all__ = [
    "PipelineManager",
    "PipelineError",
    "PipelineStage",
    "ItemStatus",
    "PipelineItem"
]