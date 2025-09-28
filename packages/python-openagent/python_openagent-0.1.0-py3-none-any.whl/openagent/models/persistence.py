"""
Persistence models for execution state management.

This module defines the data structures used for saving and loading
execution state to enable recovery from interruptions.
"""

from datetime import datetime
from typing import Dict, Any, Optional, List
from enum import Enum
from pydantic import BaseModel, Field

from openagent.core.execution_interfaces import BaseExecutionOutput, ExecutionStatus


class ExecutionPhase(Enum):
    """Phases of execution lifecycle."""

    INITIALIZED = "initialized"
    PLANNING = "planning"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    INTERRUPTED = "interrupted"


class StepState(BaseModel):
    """State of an individual execution step."""

    step_id: int = Field(..., description="Step identifier")
    status: ExecutionStatus = Field(
        default=ExecutionStatus.PENDING, description="Current step status"
    )
    start_time: Optional[datetime] = Field(
        default=None, description="Step start timestamp"
    )
    end_time: Optional[datetime] = Field(
        default=None, description="Step completion timestamp"
    )
    execution_time_ms: Optional[int] = Field(
        default=None, description="Execution time in milliseconds"
    )
    result: Optional[Dict[str, Any]] = Field(
        default=None, description="Step result as serializable dict"
    )
    error_message: Optional[str] = Field(
        default=None, description="Error message if step failed"
    )
    retry_count: int = Field(default=0, description="Number of retry attempts made")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class ExecutionState(BaseModel):
    """Complete execution state for persistence."""

    execution_id: str = Field(..., description="Unique execution identifier (UUID)")
    phase: ExecutionPhase = Field(
        default=ExecutionPhase.INITIALIZED, description="Current execution phase"
    )

    # Execution metadata
    created_at: datetime = Field(
        default_factory=datetime.now, description="Execution creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=datetime.now, description="Last update timestamp"
    )
    started_at: Optional[datetime] = Field(
        default=None, description="Execution start timestamp"
    )
    completed_at: Optional[datetime] = Field(
        default=None, description="Execution completion timestamp"
    )

    # Original query and plan
    original_query: Optional[str] = Field(
        default=None, description="Original user query"
    )
    execution_plan: Optional[Dict[str, Any]] = Field(
        default=None, description="Serialized execution plan"
    )
    execution_order: List[int] = Field(
        default_factory=list, description="Planned execution order"
    )

    # Step tracking
    step_states: Dict[int, StepState] = Field(
        default_factory=dict, description="State of each step"
    )
    completed_steps: List[int] = Field(
        default_factory=list, description="List of completed step IDs"
    )
    failed_steps: List[int] = Field(
        default_factory=list, description="List of failed step IDs"
    )
    current_batch: List[int] = Field(
        default_factory=list, description="Currently executing step batch"
    )

    # Execution results
    overall_success: bool = Field(
        default=False, description="Overall execution success status"
    )
    total_execution_time_ms: int = Field(default=0, description="Total execution time")

    # Configuration snapshot
    config_snapshot: Dict[str, Any] = Field(
        default_factory=dict, description="Configuration used for execution"
    )

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}

    def update_timestamp(self):
        """Update the last modified timestamp."""
        self.updated_at = datetime.now()

    def mark_step_started(self, step_id: int):
        """Mark a step as started."""
        if step_id not in self.step_states:
            self.step_states[step_id] = StepState(step_id=step_id)

        self.step_states[step_id].status = ExecutionStatus.RUNNING
        self.step_states[step_id].start_time = datetime.now()
        self.update_timestamp()

    def mark_step_completed(
        self, step_id: int, result: BaseExecutionOutput, execution_time_ms: int
    ):
        """Mark a step as completed with results."""
        if step_id not in self.step_states:
            self.step_states[step_id] = StepState(step_id=step_id)

        step_state = self.step_states[step_id]
        step_state.status = (
            ExecutionStatus.COMPLETED if result.success else ExecutionStatus.FAILED
        )
        step_state.end_time = datetime.now()
        step_state.execution_time_ms = execution_time_ms

        # Serialize result for storage
        try:
            step_state.result = (
                result.model_dump()
                if hasattr(result, "model_dump")
                else result.__dict__
            )
        except Exception:
            step_state.result = {
                "success": result.success,
                "result": str(getattr(result, "result", None)),
            }

        if not result.success:
            step_state.error_message = result.error_message
            if step_id not in self.failed_steps:
                self.failed_steps.append(step_id)
        else:
            if step_id not in self.completed_steps:
                self.completed_steps.append(step_id)

        self.update_timestamp()

    def mark_step_failed(self, step_id: int, error_message: str):
        """Mark a step as failed."""
        if step_id not in self.step_states:
            self.step_states[step_id] = StepState(step_id=step_id)

        step_state = self.step_states[step_id]
        step_state.status = ExecutionStatus.FAILED
        step_state.end_time = datetime.now()
        step_state.error_message = error_message

        if step_id not in self.failed_steps:
            self.failed_steps.append(step_id)

        self.update_timestamp()

    def get_resumable_steps(self) -> List[int]:
        """Get list of steps that can be resumed (not completed, not failed)."""
        resumable = []
        for step_id, step_state in self.step_states.items():
            if step_state.status in [ExecutionStatus.PENDING, ExecutionStatus.RUNNING]:
                resumable.append(step_id)
        return resumable

    def get_completion_percentage(self) -> float:
        """Calculate execution completion percentage."""
        if not self.step_states:
            return 0.0

        completed_count = len(self.completed_steps)
        total_steps = len(self.step_states)
        return (completed_count / total_steps) * 100.0

    def can_resume(self) -> bool:
        """Check if execution can be resumed."""
        return (
            self.phase in [ExecutionPhase.EXECUTING, ExecutionPhase.INTERRUPTED]
            and len(self.completed_steps) < len(self.step_states)
            and self.execution_plan is not None
        )


class PersistenceMetadata(BaseModel):
    """Metadata for persistence files."""

    execution_id: str = Field(..., description="Execution identifier")
    file_type: str = Field(..., description="Type of persistence file")
    created_at: datetime = Field(
        default_factory=datetime.now, description="File creation timestamp"
    )
    file_size: int = Field(default=0, description="File size in bytes")
    checksum: Optional[str] = Field(
        default=None, description="File checksum for integrity"
    )

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}
