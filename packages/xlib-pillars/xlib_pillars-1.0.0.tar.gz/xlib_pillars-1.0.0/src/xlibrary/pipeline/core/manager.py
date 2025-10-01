"""
Pipeline Management Core

Universal pipeline manager for tracking items through multi-stage workflows.
Completely agnostic to use case - can be used for any process that moves
items through defined stages.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, Callable
from datetime import datetime

from .types import (
    PipelineItem, PipelineStage, StageResult, ItemStatus, 
    StageStatus, PipelineStatistics
)


class PipelineError(Exception):
    """Base exception for pipeline operations."""
    pass


class PipelineManager:
    """
    Universal pipeline state management system.
    
    Tracks items through configurable stages with full state persistence,
    error handling, and recovery capabilities. Completely agnostic to use case.
    """
    
    def __init__(self, index_file: Union[str, Path], stages: List[Union[str, PipelineStage]] = None):
        """
        Initialize pipeline manager.
        
        Args:
            index_file: Path to JSON file for state persistence
            stages: List of stage names or PipelineStage objects
        """
        self.index_file = Path(index_file)
        self.index_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Configure stages
        self.stages: Dict[str, PipelineStage] = {}
        if stages:
            for stage in stages:
                if isinstance(stage, str):
                    self.stages[stage] = PipelineStage(name=stage)
                else:
                    self.stages[stage.name] = stage
        
        # Load or initialize index
        self.items: Dict[str, PipelineItem] = {}
        self.metadata: Dict[str, Any] = {}
        self._load_index()
    
    def _load_index(self) -> None:
        """Load existing index or create new one."""
        if self.index_file.exists():
            try:
                with open(self.index_file, 'r') as f:
                    data = json.load(f)
                
                # Load metadata
                self.metadata = data.get("metadata", {})
                
                # Load items
                for item_id, item_data in data.get("items", {}).items():
                    self.items[item_id] = PipelineItem.from_dict(item_data)
                    
            except Exception as e:
                raise PipelineError(f"Failed to load index from {self.index_file}: {e}")
        else:
            # Initialize new index
            self.metadata = {
                "created": datetime.now().isoformat(),
                "version": "1.0",
                "stages": [stage.name for stage in self.stages.values()]
            }
            self._save_index()
    
    def _save_index(self) -> None:
        """Save current state to index file."""
        try:
            # Update metadata
            self.metadata.update({
                "last_updated": datetime.now().isoformat(),
                "total_items": len(self.items),
                "stages": [stage.name for stage in self.stages.values()]
            })
            
            # Serialize to JSON
            data = {
                "metadata": self.metadata,
                "items": {
                    item_id: item.to_dict()
                    for item_id, item in self.items.items()
                }
            }
            
            with open(self.index_file, 'w') as f:
                json.dump(data, f, indent=2, default=str)
                
        except Exception as e:
            raise PipelineError(f"Failed to save index to {self.index_file}: {e}")
    
    def _calculate_file_hash(self, file_path: Path) -> Optional[str]:
        """Calculate SHA256 hash of file."""
        if not file_path.exists():
            return None
        
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()[:8]  # First 8 chars
        except Exception:
            return None
    
    def add_item(self, item_id: str, source_file: Optional[Path] = None, 
                metadata: Dict[str, Any] = None) -> PipelineItem:
        """
        Add a new item to the pipeline.
        
        Args:
            item_id: Unique identifier for the item
            source_file: Optional source file path
            metadata: Additional metadata
            
        Returns:
            Created PipelineItem
        """
        if item_id in self.items:
            raise PipelineError(f"Item {item_id} already exists")
        
        # Calculate source file hash
        source_hash = None
        if source_file:
            source_hash = self._calculate_file_hash(source_file)
        
        # Create new item
        now = datetime.now()
        item = PipelineItem(
            item_id=item_id,
            created_at=now,
            updated_at=now,
            status=ItemStatus.NEW,
            source_file=source_file,
            source_hash=source_hash,
            metadata=metadata or {}
        )
        
        self.items[item_id] = item
        self._save_index()
        return item
    
    def update_stage(self, item_id: str, stage_name: str, 
                    status: Union[str, StageStatus] = StageStatus.COMPLETED,
                    input_file: Optional[Path] = None,
                    output_file: Optional[Path] = None,
                    metadata: Dict[str, Any] = None,
                    error: Optional[str] = None) -> None:
        """
        Update a stage for an item.
        
        Args:
            item_id: Item identifier
            stage_name: Stage to update
            status: Stage status
            input_file: Input file for this stage
            output_file: Output file produced by this stage
            metadata: Stage-specific metadata
            error: Error message if stage failed
        """
        if item_id not in self.items:
            raise PipelineError(f"Item {item_id} not found")
        
        if isinstance(status, str):
            status = StageStatus(status)
        
        item = self.items[item_id]
        now = datetime.now()
        
        # Create or update stage result
        if stage_name in item.stages:
            stage_result = item.stages[stage_name]
            stage_result.completed_at = now
            stage_result.status = status
        else:
            stage_result = StageResult(
                stage_name=stage_name,
                status=StageStatus.RUNNING,
                started_at=now
            )
            item.stages[stage_name] = stage_result
        
        # Update stage result
        stage_result.status = status
        stage_result.completed_at = now
        stage_result.input_file = input_file
        stage_result.output_file = output_file
        stage_result.metadata.update(metadata or {})
        stage_result.error = error
        
        # Update item status and current stage
        item.updated_at = now
        item.current_stage = stage_name
        
        if status == StageStatus.FAILED:
            item.status = ItemStatus.FAILED
            # Add error to item error list
            item.errors.append({
                "stage": stage_name,
                "error": error,
                "timestamp": now.isoformat()
            })
        elif status == StageStatus.COMPLETED:
            # Check if all required stages are complete
            stage_names = [s.name for s in self.stages.values() if s.required]
            completed_stages = [
                name for name, result in item.stages.items()
                if result.status == StageStatus.COMPLETED and name in stage_names
            ]
            
            if len(completed_stages) == len(stage_names):
                item.status = ItemStatus.COMPLETED
            else:
                item.status = ItemStatus.IN_PROGRESS
        
        self._save_index()
    
    def get_item(self, item_id: str) -> Optional[PipelineItem]:
        """Get an item by ID."""
        return self.items.get(item_id)
    
    def get_items_by_status(self, status: Union[str, ItemStatus]) -> List[PipelineItem]:
        """Get all items with a specific status."""
        if isinstance(status, str):
            status = ItemStatus(status)
        
        return [item for item in self.items.values() if item.status == status]
    
    def get_items_at_stage(self, stage_name: str) -> List[PipelineItem]:
        """Get all items currently at a specific stage."""
        return [
            item for item in self.items.values()
            if item.current_stage == stage_name
        ]
    
    def get_failed_items(self) -> List[PipelineItem]:
        """Get all items that have failed."""
        return self.get_items_by_status(ItemStatus.FAILED)
    
    def retry_failed_item(self, item_id: str, from_stage: Optional[str] = None) -> None:
        """
        Retry processing for a failed item.
        
        Args:
            item_id: Item to retry
            from_stage: Stage to restart from (if None, restarts from failed stage)
        """
        if item_id not in self.items:
            raise PipelineError(f"Item {item_id} not found")
        
        item = self.items[item_id]
        
        if from_stage:
            # Clear stages from the specified stage onward
            stage_names = list(self.stages.keys())
            if from_stage in stage_names:
                start_idx = stage_names.index(from_stage)
                for stage_name in stage_names[start_idx:]:
                    if stage_name in item.stages:
                        del item.stages[stage_name]
            
            item.current_stage = from_stage
            item.status = ItemStatus.IN_PROGRESS
        else:
            # Just reset status to allow retry
            item.status = ItemStatus.IN_PROGRESS
        
        item.updated_at = datetime.now()
        self._save_index()
    
    def delete_item(self, item_id: str) -> bool:
        """
        Delete an item from the pipeline.
        
        Returns:
            True if item was deleted, False if not found
        """
        if item_id in self.items:
            del self.items[item_id]
            self._save_index()
            return True
        return False
    
    def get_statistics(self) -> PipelineStatistics:
        """Get comprehensive pipeline statistics."""
        # Status breakdown
        status_counts = {}
        for status in ItemStatus:
            status_counts[status.value] = len(self.get_items_by_status(status))
        
        # Current stage breakdown
        stage_counts = {}
        for stage_name in self.stages.keys():
            stage_counts[stage_name] = len(self.get_items_at_stage(stage_name))
        
        # Stage performance analysis
        stage_performance = {}
        processing_times = {}
        
        for stage_name in self.stages.keys():
            stage_results = []
            durations = []
            
            for item in self.items.values():
                if stage_name in item.stages:
                    result = item.stages[stage_name]
                    stage_results.append(result)
                    if result.duration_seconds:
                        durations.append(result.duration_seconds)
            
            # Calculate performance metrics
            completed = len([r for r in stage_results if r.status == StageStatus.COMPLETED])
            failed = len([r for r in stage_results if r.status == StageStatus.FAILED])
            avg_duration = sum(durations) / len(durations) if durations else 0
            
            stage_performance[stage_name] = {
                "total_processed": len(stage_results),
                "completed": completed,
                "failed": failed,
                "success_rate": completed / len(stage_results) if stage_results else 0,
                "average_duration": avg_duration
            }
            processing_times[stage_name] = avg_duration
        
        # Error summary
        error_summary = []
        for item in self.items.values():
            for error in item.errors:
                error_summary.append({
                    "item_id": item.item_id,
                    "stage": error.get("stage"),
                    "error": error.get("error"),
                    "timestamp": error.get("timestamp")
                })
        
        return PipelineStatistics(
            total_items=len(self.items),
            by_status=status_counts,
            by_current_stage=stage_counts,
            stage_performance=stage_performance,
            error_summary=error_summary[-10:],  # Last 10 errors
            processing_time=processing_times
        )
    
    def export_data(self, include_metadata: bool = True) -> Dict[str, Any]:
        """Export all pipeline data as dictionary."""
        data = {
            "items": [item.to_dict() for item in self.items.values()],
            "statistics": self.get_statistics().to_dict()
        }
        
        if include_metadata:
            data["metadata"] = self.metadata
            data["stages"] = [
                {
                    "name": stage.name,
                    "description": stage.description,
                    "required": stage.required,
                    "timeout_seconds": stage.timeout_seconds,
                    "retry_attempts": stage.retry_attempts
                }
                for stage in self.stages.values()
            ]
        
        return data