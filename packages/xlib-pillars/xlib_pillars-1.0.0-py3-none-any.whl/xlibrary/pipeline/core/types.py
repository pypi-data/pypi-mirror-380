"""
Type definitions for pipeline management.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from pathlib import Path


class ItemStatus(Enum):
    """Overall status of an item in the pipeline."""
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ARCHIVED = "archived"


class StageStatus(Enum):
    """Status of a specific pipeline stage."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class PipelineStage:
    """Configuration for a pipeline stage."""
    name: str
    description: str = ""
    required: bool = True
    timeout_seconds: Optional[int] = None
    retry_attempts: int = 0
    dependencies: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class StageResult:
    """Result of processing a stage."""
    stage_name: str
    status: StageStatus
    started_at: datetime
    completed_at: Optional[datetime] = None
    input_file: Optional[Path] = None
    output_file: Optional[Path] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    
    @property
    def duration_seconds(self) -> Optional[float]:
        """Calculate processing duration."""
        if self.completed_at and self.started_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None


@dataclass
class PipelineItem:
    """An item being tracked through the pipeline."""
    item_id: str
    created_at: datetime
    updated_at: datetime
    status: ItemStatus
    current_stage: Optional[str] = None
    source_file: Optional[Path] = None
    source_hash: Optional[str] = None
    stages: Dict[str, StageResult] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    errors: List[Dict[str, Any]] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "item_id": self.item_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(), 
            "status": self.status.value,
            "current_stage": self.current_stage,
            "source_file": str(self.source_file) if self.source_file else None,
            "source_hash": self.source_hash,
            "stages": {
                name: {
                    "stage_name": result.stage_name,
                    "status": result.status.value,
                    "started_at": result.started_at.isoformat(),
                    "completed_at": result.completed_at.isoformat() if result.completed_at else None,
                    "input_file": str(result.input_file) if result.input_file else None,
                    "output_file": str(result.output_file) if result.output_file else None,
                    "metadata": result.metadata,
                    "error": result.error,
                    "duration_seconds": result.duration_seconds
                }
                for name, result in self.stages.items()
            },
            "metadata": self.metadata,
            "errors": self.errors
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PipelineItem":
        """Create from dictionary (JSON deserialization)."""
        item = cls(
            item_id=data["item_id"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            status=ItemStatus(data["status"]),
            current_stage=data.get("current_stage"),
            source_file=Path(data["source_file"]) if data.get("source_file") else None,
            source_hash=data.get("source_hash"),
            metadata=data.get("metadata", {}),
            errors=data.get("errors", [])
        )
        
        # Reconstruct stage results
        for stage_name, stage_data in data.get("stages", {}).items():
            item.stages[stage_name] = StageResult(
                stage_name=stage_data["stage_name"],
                status=StageStatus(stage_data["status"]),
                started_at=datetime.fromisoformat(stage_data["started_at"]),
                completed_at=datetime.fromisoformat(stage_data["completed_at"]) if stage_data.get("completed_at") else None,
                input_file=Path(stage_data["input_file"]) if stage_data.get("input_file") else None,
                output_file=Path(stage_data["output_file"]) if stage_data.get("output_file") else None,
                metadata=stage_data.get("metadata", {}),
                error=stage_data.get("error")
            )
        
        return item


@dataclass
class PipelineStatistics:
    """Statistics about pipeline processing."""
    total_items: int
    by_status: Dict[str, int]
    by_current_stage: Dict[str, int]
    stage_performance: Dict[str, Dict[str, Any]]
    error_summary: List[Dict[str, Any]]
    processing_time: Dict[str, float]  # Average time per stage
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "total_items": self.total_items,
            "by_status": self.by_status,
            "by_current_stage": self.by_current_stage,
            "stage_performance": self.stage_performance,
            "error_summary": self.error_summary,
            "processing_time": self.processing_time
        }