"""
Real-time execution status models for frontend monitoring.

This module provides detailed status tracking for execution progress,
including step-level states, dependency tracking, and progress estimation.
"""

from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field

from openagent.core.execution_interfaces import ExecutionStatus


class StepDependencyStatus(str, Enum):
    """Status of step dependencies."""

    ALL_COMPLETED = "all_completed"
    WAITING_FOR_DEPS = "waiting_for_deps"
    BLOCKED = "blocked"
    DEPENDENCY_FAILED = "dependency_failed"


class ExecutionProgressPhase(str, Enum):
    """High-level execution progress phases."""

    NOT_STARTED = "not_started"
    INITIALIZING = "initializing"
    RUNNING = "running"
    COMPLETING = "completing"
    COMPLETED = "completed"
    FAILED = "failed"
    INTERRUPTED = "interrupted"


class StepProgress(BaseModel):
    """Real-time progress information for a single step."""

    step_id: int
    status: ExecutionStatus
    dependency_status: StepDependencyStatus
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    elapsed_ms: Optional[int] = None
    estimated_remaining_ms: Optional[int] = None
    error_message: Optional[str] = None
    output_preview: Optional[str] = None
    waiting_for_steps: List[int] = Field(default_factory=list)


class ExecutionStatusSummary(BaseModel):
    """Comprehensive execution status for frontend consumption."""

    # Basic execution info
    execution_id: str = Field(..., description="Unique execution identifier")
    query: Optional[str] = Field(default=None, description="Original user query")
    phase: ExecutionProgressPhase = Field(default=ExecutionProgressPhase.NOT_STARTED)

    # Timing information
    started_at: Optional[datetime] = Field(
        default=None, description="Execution start time"
    )
    last_updated: datetime = Field(
        default_factory=datetime.now, description="Last status update"
    )
    estimated_completion: Optional[datetime] = Field(
        default=None, description="Estimated completion time"
    )

    # Step-level details
    total_steps: int = Field(..., description="Total number of steps in execution plan")
    steps_completed: int = Field(default=0, description="Number of completed steps")
    steps_running: int = Field(
        default=0, description="Number of currently running steps"
    )
    steps_queued: int = Field(default=0, description="Number of queued steps")
    steps_failed: int = Field(default=0, description="Number of failed steps")

    # Progress metrics
    completion_percentage: float = Field(
        default=0.0, description="Overall completion percentage"
    )
    estimated_remaining_minutes: Optional[float] = Field(
        default=None, description="Estimated minutes remaining"
    )

    # Detailed step information
    step_details: Dict[int, StepProgress] = Field(
        default_factory=dict, description="Detailed step progress"
    )
    currently_running_steps: List[int] = Field(
        default_factory=list, description="Steps currently executing"
    )
    next_queued_steps: List[int] = Field(
        default_factory=list, description="Next steps ready to run"
    )
    blocked_steps: List[int] = Field(
        default_factory=list, description="Steps blocked by dependencies"
    )

    # Execution flow information
    execution_order: List[int] = Field(
        default_factory=list, description="Planned execution order"
    )
    dependency_map: Dict[int, List[int]] = Field(
        default_factory=dict, description="Step dependency relationships"
    )

    # Performance metrics
    average_step_time_ms: Optional[float] = Field(
        default=None, description="Average time per completed step"
    )
    throughput_steps_per_minute: Optional[float] = Field(
        default=None, description="Steps completed per minute"
    )

    # Error and warning information
    has_errors: bool = Field(default=False, description="Whether any steps have errors")
    error_summary: List[str] = Field(
        default_factory=list, description="Summary of errors encountered"
    )
    warnings: List[str] = Field(
        default_factory=list, description="Non-critical warnings"
    )

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}

    def get_status_summary(self) -> str:
        """Get a human-readable status summary."""
        if self.phase == ExecutionProgressPhase.COMPLETED:
            return f"Completed all {self.total_steps} steps"
        elif self.phase == ExecutionProgressPhase.FAILED:
            return f"Failed with {self.steps_failed} failed steps"
        elif self.phase == ExecutionProgressPhase.RUNNING:
            return f"Running: {self.steps_completed}/{self.total_steps} complete, {self.steps_running} active"
        else:
            return f"Phase: {self.phase.value}"

    def get_next_steps_info(self) -> str:
        """Get information about what's happening next."""
        if self.currently_running_steps:
            running = ", ".join(map(str, self.currently_running_steps))
            info = f"Running steps: {running}"
        else:
            info = "No steps currently running"

        if self.next_queued_steps:
            queued = ", ".join(map(str, self.next_queued_steps[:3]))
            info += f" | Next: {queued}"
            if len(self.next_queued_steps) > 3:
                info += f" (+{len(self.next_queued_steps) - 3} more)"

        if self.blocked_steps:
            info += (
                f" | Blocked: {len(self.blocked_steps)} steps waiting on dependencies"
            )

        return info


class ExecutionStatusTracker:
    """
    Tracks real-time execution status for frontend monitoring.

    This class maintains detailed state about step execution progress,
    dependencies, timing, and provides methods for querying status.
    """

    def __init__(
        self, execution_id: str, execution_plan: Any, query: Optional[str] = None
    ):
        """Initialize status tracker for an execution."""
        self.execution_id = execution_id
        self.query = query
        self.execution_plan = execution_plan
        self.started_at = datetime.now()
        self.last_updated = datetime.now()

        # Initialize step tracking
        self.step_progress: Dict[int, StepProgress] = {}
        self.dependency_map: Dict[int, List[int]] = {}
        self.execution_order: List[int] = []

        # Build dependency map from execution plan
        self._build_dependency_map()

        # Initialize all steps as queued
        self._initialize_step_states()

    def _build_dependency_map(self):
        """Build dependency relationships from execution plan."""
        try:
            self.execution_order, _ = self.execution_plan.get_execution_order()

            for entry in self.execution_plan.entries:
                step_id = entry.queue_position
                dependencies = [dep.dependency_index for dep in entry.dependency]
                self.dependency_map[step_id] = dependencies

        except Exception:
            # Fallback to simple sequential order
            self.execution_order = [
                entry.queue_position for entry in self.execution_plan.entries
            ]
            self.dependency_map = {step_id: [] for step_id in self.execution_order}

    def _initialize_step_states(self):
        """Initialize all steps with appropriate initial status."""
        for step_id in self.execution_order:
            dependencies = self.dependency_map.get(step_id, [])

            if not dependencies:
                # No dependencies - ready to run
                dep_status = StepDependencyStatus.ALL_COMPLETED
            else:
                # Has dependencies - waiting
                dep_status = StepDependencyStatus.WAITING_FOR_DEPS

            self.step_progress[step_id] = StepProgress(
                step_id=step_id,
                status=ExecutionStatus.PENDING,
                dependency_status=dep_status,
                waiting_for_steps=dependencies.copy(),
            )

    def mark_step_started(self, step_id: int):
        """Mark a step as started."""
        if step_id in self.step_progress:
            step = self.step_progress[step_id]
            step.status = ExecutionStatus.RUNNING
            step.dependency_status = StepDependencyStatus.ALL_COMPLETED
            step.start_time = datetime.now()
            step.waiting_for_steps = []

        self._update_dependent_steps(step_id)
        self.last_updated = datetime.now()

    def mark_step_completed(
        self,
        step_id: int,
        success: bool = True,
        output_preview: Optional[str] = None,
        error_message: Optional[str] = None,
    ):
        """Mark a step as completed (successfully or failed)."""
        if step_id in self.step_progress:
            step = self.step_progress[step_id]
            step.status = (
                ExecutionStatus.COMPLETED if success else ExecutionStatus.FAILED
            )
            step.end_time = datetime.now()
            step.output_preview = output_preview
            step.error_message = error_message

            if step.start_time:
                elapsed = step.end_time - step.start_time
                step.elapsed_ms = int(elapsed.total_seconds() * 1000)

        self._update_dependent_steps(step_id)
        self.last_updated = datetime.now()

    def _update_dependent_steps(self, completed_step_id: int):
        """Update dependency status for steps that depend on the completed step."""
        for step_id, step in self.step_progress.items():
            if completed_step_id in step.waiting_for_steps:
                step.waiting_for_steps.remove(completed_step_id)

                # Update dependency status
                if not step.waiting_for_steps:
                    step.dependency_status = StepDependencyStatus.ALL_COMPLETED
                elif any(
                    self.step_progress[dep].status == ExecutionStatus.FAILED
                    for dep in self.dependency_map.get(step_id, [])
                ):
                    step.dependency_status = StepDependencyStatus.DEPENDENCY_FAILED
                else:
                    step.dependency_status = StepDependencyStatus.WAITING_FOR_DEPS

    def get_status_summary(self) -> ExecutionStatusSummary:
        """Get comprehensive status summary for frontend consumption."""

        # Count step statuses
        completed = sum(
            1
            for s in self.step_progress.values()
            if s.status == ExecutionStatus.COMPLETED
        )
        running = sum(
            1
            for s in self.step_progress.values()
            if s.status == ExecutionStatus.RUNNING
        )
        failed = sum(
            1 for s in self.step_progress.values() if s.status == ExecutionStatus.FAILED
        )
        queued = len(self.step_progress) - completed - running - failed

        # Determine overall phase
        if failed > 0:
            phase = ExecutionProgressPhase.FAILED
        elif completed == len(self.step_progress):
            phase = ExecutionProgressPhase.COMPLETED
        elif running > 0 or completed > 0:
            phase = ExecutionProgressPhase.RUNNING
        else:
            phase = ExecutionProgressPhase.NOT_STARTED

        # Calculate progress metrics
        completion_pct = (
            (completed / len(self.step_progress)) * 100 if self.step_progress else 0
        )

        # Get step lists
        currently_running = [
            s.step_id
            for s in self.step_progress.values()
            if s.status == ExecutionStatus.RUNNING
        ]
        next_queued = [
            s.step_id
            for s in self.step_progress.values()
            if s.status == ExecutionStatus.PENDING
            and s.dependency_status == StepDependencyStatus.ALL_COMPLETED
        ][:5]
        blocked = [
            s.step_id
            for s in self.step_progress.values()
            if s.status == ExecutionStatus.PENDING
            and s.dependency_status == StepDependencyStatus.WAITING_FOR_DEPS
        ]

        # Performance calculations
        completed_steps = [
            s
            for s in self.step_progress.values()
            if s.status == ExecutionStatus.COMPLETED and s.elapsed_ms is not None
        ]
        avg_time = (
            sum(s.elapsed_ms for s in completed_steps if s.elapsed_ms is not None)
            / len(completed_steps)
            if completed_steps
            else None
        )

        # Error summary
        errors = [
            s.error_message for s in self.step_progress.values() if s.error_message
        ]

        return ExecutionStatusSummary(
            execution_id=self.execution_id,
            query=self.query,
            phase=phase,
            started_at=self.started_at,
            last_updated=self.last_updated,
            total_steps=len(self.step_progress),
            steps_completed=completed,
            steps_running=running,
            steps_queued=queued,
            steps_failed=failed,
            completion_percentage=completion_pct,
            step_details=self.step_progress,
            currently_running_steps=currently_running,
            next_queued_steps=next_queued,
            blocked_steps=blocked,
            execution_order=self.execution_order,
            dependency_map=self.dependency_map,
            average_step_time_ms=avg_time,
            has_errors=len(errors) > 0,
            error_summary=errors[:5],  # Limit to first 5 errors
        )
