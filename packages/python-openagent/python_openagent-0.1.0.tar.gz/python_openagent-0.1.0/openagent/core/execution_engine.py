"""
Production-ready execution engine for OpenAgent.

This module provides a configurable, thread-safe execution engine that processes
execution plans with parallel execution, dependency resolution, and output pattern replacement.
"""

import asyncio
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from typing import Dict, Any, List, Set, Optional
from dataclasses import dataclass
from datetime import datetime
import logging
from threading import Lock

from openagent.models.scheduling import (
    ExecutionPlan,
    ExecutionPlanEntry,
    ExecutionHandler,
)
from openagent.config.config import OpenAgentConfig
from openagent.core.execution_interfaces import (
    AbstractExecutionHandler,
    BaseExecutionOutput,
    ExecutionContext,
    ExecutionResult,
    ExecutionStatus,
    ExecutionError,
)
from openagent.core.persistence_manager import PersistenceManager
from openagent.models.persistence import ExecutionState, ExecutionPhase
from openagent.models.status_tracking import (
    ExecutionStatusTracker,
    ExecutionStatusSummary,
)

logger = logging.getLogger(__name__)


@dataclass
class ExecutionStep:
    """Internal representation of an execution step with its status and result."""

    entry: ExecutionPlanEntry
    status: ExecutionStatus = ExecutionStatus.PENDING
    result: Optional[BaseExecutionOutput] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    future: Optional[Future] = None


class ExecutionEngine:
    """
    Production-ready execution engine that processes ExecutionPlan objects.

    Features:
    - Parallel execution of independent steps
    - Dependency resolution with topological sorting
    - Output pattern replacement ({{%%output_step_N%%}})
    - Thread-safe operation
    - Configurable thread pool and timeouts
    - Comprehensive error handling and logging
    """

    def __init__(self, config: OpenAgentConfig):
        """
        Initialize the execution engine.

        Args:
            config: OpenAgent configuration object
        """
        self.config = config
        self._handler_registry: Dict[ExecutionHandler, AbstractExecutionHandler] = {}
        self._lock = Lock()

        # Initialize persistence manager
        self.persistence_manager = PersistenceManager(config)

        # Real-time status tracking
        self._active_status_trackers: Dict[str, ExecutionStatusTracker] = {}
        self._tracker_lock = Lock()

        # Auto-resume interrupted executions if enabled
        if config.execution_persistence_enabled and config.execution_auto_resume:
            self._auto_resume_executions()

    def register_handler(
        self, handler_type: ExecutionHandler, handler_instance: AbstractExecutionHandler
    ) -> None:
        """
        Register a handler for a specific execution type.

        Args:
            handler_type: The type of execution this handler processes
            handler_instance: The handler implementation
        """
        with self._lock:
            self._handler_registry[handler_type] = handler_instance
            logger.info(f"Registered handler for {handler_type.value}")

    def unregister_handler(self, handler_type: ExecutionHandler) -> None:
        """Remove a handler from the registry."""
        with self._lock:
            if handler_type in self._handler_registry:
                del self._handler_registry[handler_type]
                logger.info(f"Unregistered handler for {handler_type.value}")

    def get_registered_handlers(self) -> List[ExecutionHandler]:
        """Get list of registered handler types."""
        with self._lock:
            return list(self._handler_registry.keys())

    def _auto_resume_executions(self):
        """Automatically resume interrupted executions on startup."""
        try:
            resumable_executions = self.persistence_manager.find_resumable_executions()

            if resumable_executions:
                logger.info(f"Found {len(resumable_executions)} resumable executions")
                for execution_state in resumable_executions:
                    logger.info(
                        f"Resumable execution: {execution_state.execution_id} "
                        f"({execution_state.get_completion_percentage():.1f}% complete)"
                    )
            else:
                logger.debug("No resumable executions found")

        except Exception as e:
            logger.error(f"Failed to check for resumable executions: {str(e)}")

    async def resume_execution(self, execution_plan: ExecutionPlan) -> ExecutionResult:
        """
        Resume an interrupted execution using the ExecutionPlan with matching execution_id.

        Args:
            execution_plan: ExecutionPlan with execution_id matching the saved state

        Returns:
            ExecutionResult from resumed execution

        Raises:
            ExecutionError: If resuming fails or execution is in non-resumable state
        """
        if not self.persistence_manager:
            raise ExecutionError(
                "Persistence manager not available for resuming executions"
            )

        execution_id = execution_plan.execution_id
        execution_state = self.persistence_manager.load_execution_state(execution_id)
        if not execution_state:
            raise ExecutionError(f"No execution state found for ID: {execution_id}")

        if execution_state.phase in [ExecutionPhase.COMPLETED, ExecutionPhase.FAILED]:
            raise ExecutionError(
                f"Cannot resume execution {execution_id} - already in final state: {execution_state.phase.value}"
            )

        logger.info(
            f"Resuming execution {execution_id} from phase {execution_state.phase.value}"
        )

        # Resume execution using the provided ExecutionPlan
        return await self.execute(execution_plan)

    def get_execution_status(self, execution_id: str) -> Optional["ExecutionState"]:
        """Get the current status of an execution."""
        if not self.persistence_manager:
            return None
        return self.persistence_manager.load_execution_state(execution_id)

    def get_real_time_status(
        self, execution_id: str
    ) -> Optional[ExecutionStatusSummary]:
        """
        Get real-time execution status with detailed step information.

        Args:
            execution_id: The execution ID to get status for

        Returns:
            ExecutionStatusSummary with detailed step progress, or None if not found
        """
        with self._tracker_lock:
            if execution_id in self._active_status_trackers:
                return self._active_status_trackers[execution_id].get_status_summary()

        # If not in active trackers, check persistence
        if self.persistence_manager:
            execution_state = self.persistence_manager.load_execution_state(
                execution_id
            )
            if execution_state:
                # Create a summary from persistent state
                from openagent.models.status_tracking import (
                    ExecutionStatusSummary,
                    ExecutionProgressPhase,
                )

                if execution_state.phase == ExecutionPhase.COMPLETED:
                    phase = ExecutionProgressPhase.COMPLETED
                elif execution_state.phase == ExecutionPhase.FAILED:
                    phase = ExecutionProgressPhase.FAILED
                elif execution_state.phase == ExecutionPhase.EXECUTING:
                    phase = ExecutionProgressPhase.RUNNING
                else:
                    phase = ExecutionProgressPhase.NOT_STARTED

                completed = sum(
                    1
                    for step in execution_state.step_states.values()
                    if step.status == ExecutionStatus.COMPLETED
                )
                failed = sum(
                    1
                    for step in execution_state.step_states.values()
                    if step.status == ExecutionStatus.FAILED
                )
                total = len(execution_state.step_states)

                return ExecutionStatusSummary(
                    execution_id=execution_id,
                    query=execution_state.original_query,
                    phase=phase,
                    started_at=execution_state.started_at,
                    last_updated=execution_state.updated_at,
                    total_steps=total,
                    steps_completed=completed,
                    steps_failed=failed,
                    completion_percentage=(completed / total * 100) if total > 0 else 0,
                    has_errors=failed > 0,
                )

        return None

    def list_active_executions(self) -> List[str]:
        """Get list of currently active execution IDs."""
        with self._tracker_lock:
            return list(self._active_status_trackers.keys())

    def get_all_active_statuses(self) -> Dict[str, ExecutionStatusSummary]:
        """Get real-time status for all active executions."""
        with self._tracker_lock:
            return {
                exec_id: tracker.get_status_summary()
                for exec_id, tracker in self._active_status_trackers.items()
            }

    def list_executions(self) -> List["ExecutionState"]:
        """List all saved executions."""
        if not self.persistence_manager:
            return []
        return self.persistence_manager.find_resumable_executions()

    def cleanup_old_executions(self, older_than_days: Optional[int] = None) -> int:
        """Clean up old execution files."""
        if not self.persistence_manager:
            return 0
        self.persistence_manager.cleanup_old_files()
        return 1  # Return success indicator

    async def execute(self, execution_plan: ExecutionPlan) -> ExecutionResult:
        """
        Execute the entire execution plan with automatic persistence using plan's execution_id.

        Args:
            execution_plan: The plan to execute (contains execution_id)

        Returns:
            ExecutionResult with success status and step results

        Raises:
            ExecutionError: If critical execution failure occurs
        """
        start_time = time.time()

        # Use execution ID from the plan
        execution_id = execution_plan.execution_id
        execution_state = None

        try:
            # Check if resuming from previous execution
            if self.persistence_manager and self.persistence_manager.enabled:
                execution_state = self.persistence_manager.load_execution_state(
                    execution_id
                )
                if execution_state:
                    logger.info(
                        f"Resuming execution {execution_id} from {execution_state.phase.value}"
                    )
                else:
                    # Create new execution state with plan and result tracking
                    execution_state = self.persistence_manager.create_new_execution(
                        query=getattr(execution_plan, "query", ""),
                        execution_plan=execution_plan,
                    )

            # Initialize real-time status tracking
            status_tracker = ExecutionStatusTracker(
                execution_id=execution_id,
                execution_plan=execution_plan,
                query=getattr(execution_plan, "query", None),
            )

            # Register the tracker for real-time access
            with self._tracker_lock:
                self._active_status_trackers[execution_id] = status_tracker

            # Get execution order using topological sort
            execution_order, dependency_graph = execution_plan.get_execution_order()

            # Initialize execution steps
            steps = {
                entry.queue_position: ExecutionStep(entry)
                for entry in execution_plan.entries
            }

            # Validate all required handlers are registered
            self._validate_handlers(execution_plan)

            # Update execution state to executing
            if execution_state:
                from openagent.models.persistence import ExecutionPhase

                execution_state.phase = ExecutionPhase.EXECUTING
                execution_state.execution_order = execution_order
                execution_state.started_at = datetime.now()
                execution_state.update_timestamp()
                self.persistence_manager.save_execution_state(execution_state)

            # Create thread pool
            with ThreadPoolExecutor(
                max_workers=self.config.execution_max_workers,
                thread_name_prefix="openagent-executor",
            ) as executor:
                # Execute steps with dependency resolution
                await self._execute_with_dependencies(
                    steps, execution_order, dependency_graph, executor, execution_state
                )

        except Exception as e:
            # Update execution state to failed
            if execution_state:
                from openagent.models.persistence import ExecutionPhase

                execution_state.phase = ExecutionPhase.FAILED
                execution_state.completed_at = datetime.now()
                execution_state.update_timestamp()
                self.persistence_manager.save_execution_state(execution_state)

            # Clean up the status tracker on failure
            with self._tracker_lock:
                if execution_id in self._active_status_trackers:
                    del self._active_status_trackers[execution_id]

            logger.error(f"Execution engine failed: {str(e)}")
            raise ExecutionError(
                f"Execution engine failure: {str(e)}", original_error=e
            )

        # Compile results
        end_time = time.time()
        execution_time_ms = int((end_time - start_time) * 1000)

        step_results = {}
        failed_steps = []
        overall_success = True

        for step_id, step in steps.items():
            if step.result:
                step_results[step_id] = step.result
                if not step.result.success:
                    failed_steps.append(step_id)
                    overall_success = False
            else:
                failed_steps.append(step_id)
                overall_success = False

        # Mark execution as completed in persistence
        if execution_state and self.persistence_manager:
            from openagent.models.persistence import ExecutionPhase

            execution_state.phase = ExecutionPhase.COMPLETED
            execution_state.completed_at = datetime.now()
            execution_state.overall_success = overall_success
            execution_state.total_execution_time_ms = execution_time_ms
            execution_state.failed_steps = failed_steps
            execution_state.update_timestamp()
            self.persistence_manager.save_execution_state(execution_state)

            logger.info(
                f"Execution {execution_state.execution_id} completed with success: {overall_success}"
            )

        # Clean up the status tracker
        with self._tracker_lock:
            if execution_id in self._active_status_trackers:
                del self._active_status_trackers[execution_id]

        return ExecutionResult(
            success=overall_success,
            step_results=step_results,
            total_execution_time_ms=execution_time_ms,
            failed_steps=failed_steps,
            execution_order=execution_order,
        )

    def _validate_handlers(self, execution_plan: ExecutionPlan) -> None:
        """Validate that all required handlers are registered."""
        required_handlers = {
            entry.execution_provider for entry in execution_plan.entries
        }
        missing_handlers = required_handlers - set(self._handler_registry.keys())

        if missing_handlers:
            raise ExecutionError(
                f"Missing handlers for: {[h.value for h in missing_handlers]}"
            )

    async def _execute_with_dependencies(
        self,
        steps: Dict[int, ExecutionStep],
        execution_order: List[int],
        dependency_graph: Any,
        executor: ThreadPoolExecutor,
        execution_state: Optional["ExecutionState"] = None,
    ) -> None:
        """Execute steps respecting dependencies and maximizing parallelism."""

        completed_steps: Set[int] = set()
        step_outputs: Dict[int, BaseExecutionOutput] = {}

        # Process steps in batches that can run in parallel
        remaining_steps = set(execution_order)

        while remaining_steps:
            # Find steps that can run now (all dependencies completed)
            ready_steps = []

            for step_id in remaining_steps:
                step = steps[step_id]
                dependencies = [dep.dependency_index for dep in step.entry.dependency]

                if all(dep_id in completed_steps for dep_id in dependencies):
                    ready_steps.append(step_id)

            if not ready_steps:
                # This should not happen if dependency graph is correct
                raise ExecutionError(
                    "Circular dependency or invalid execution order detected"
                )

            # Execute ready steps in parallel
            futures = {}

            for step_id in ready_steps:
                step = steps[step_id]

                # Mark step as started in persistence and real-time tracking
                if execution_state and self.persistence_manager:
                    execution_state.mark_step_started(step_id)
                    execution_state.current_batch = ready_steps
                    self.persistence_manager.save_execution_state(execution_state)

                # Update real-time status tracker
                with self._tracker_lock:
                    if (
                        execution_state
                        and execution_state.execution_id in self._active_status_trackers
                    ):
                        self._active_status_trackers[
                            execution_state.execution_id
                        ].mark_step_started(step_id)

                # Prepare input with pattern replacement
                processed_input = self._process_input_patterns(
                    step.entry.input_info, step_outputs
                )

                # Create execution context
                context = ExecutionContext(
                    step_id=step_id,
                    previous_outputs=step_outputs.copy(),
                    config=self.config.model_dump(),
                )

                # Submit for execution
                handler = self._handler_registry[step.entry.execution_provider]
                future = executor.submit(
                    self._execute_step_sync, handler, processed_input, context
                )

                futures[future] = step_id
                step.future = future
                step.status = ExecutionStatus.RUNNING
                step.start_time = time.time()

            # Wait for all parallel executions to complete
            for future in as_completed(
                futures, timeout=self.config.execution_step_timeout
            ):
                step_id = futures[future]
                step = steps[step_id]

                try:
                    result = future.result()
                    step.result = result
                    step.status = ExecutionStatus.COMPLETED
                    step_outputs[step_id] = result
                    completed_steps.add(step_id)

                    # Mark step as completed in persistence and real-time tracking
                    if execution_state and self.persistence_manager:
                        execution_time_ms = int(
                            (time.time() - (step.start_time or time.time())) * 1000
                        )
                        execution_state.mark_step_completed(
                            step_id, result, execution_time_ms
                        )
                        if step_id not in execution_state.completed_steps:
                            execution_state.completed_steps.append(step_id)
                        self.persistence_manager.save_execution_state(execution_state)

                        # Save individual step result separately
                        self.persistence_manager.save_step_result(
                            execution_state.execution_id, step_id, result
                        )

                    # Update real-time status tracker
                    with self._tracker_lock:
                        if (
                            execution_state
                            and execution_state.execution_id
                            in self._active_status_trackers
                        ):
                            output_preview = (
                                getattr(result, "content", None)
                                or str(result)[:200] + "..."
                                if len(str(result)) > 200
                                else str(result)
                            )
                            self._active_status_trackers[
                                execution_state.execution_id
                            ].mark_step_completed(
                                step_id,
                                success=result.success,
                                output_preview=output_preview,
                            )

                    logger.info(f"Step {step_id} completed successfully")

                except Exception as e:
                    step.status = ExecutionStatus.FAILED
                    error_result = BaseExecutionOutput(
                        success=False, error_message=str(e), execution_time_ms=0
                    )
                    step.result = error_result
                    step_outputs[step_id] = error_result

                    # Mark step as failed in persistence and real-time tracking
                    if execution_state and self.persistence_manager:
                        execution_time_ms = int(
                            (time.time() - (step.start_time or time.time())) * 1000
                        )
                        execution_state.mark_step_completed(
                            step_id, error_result, execution_time_ms
                        )
                        if step_id not in execution_state.failed_steps:
                            execution_state.failed_steps.append(step_id)
                        self.persistence_manager.save_execution_state(execution_state)

                        # Save individual step result separately (even for failures)
                        self.persistence_manager.save_step_result(
                            execution_state.execution_id, step_id, error_result
                        )

                    # Update real-time status tracker
                    with self._tracker_lock:
                        if (
                            execution_state
                            and execution_state.execution_id
                            in self._active_status_trackers
                        ):
                            self._active_status_trackers[
                                execution_state.execution_id
                            ].mark_step_completed(
                                step_id, success=False, error_message=str(e)
                            )

                    logger.error(f"Step {step_id} failed: {str(e)}")

                    if self.config.execution_fail_fast:
                        raise ExecutionError(
                            f"Step {step_id} failed: {str(e)}", step_id
                        )

                finally:
                    step.end_time = time.time()
                    remaining_steps.discard(step_id)

    def _execute_step_sync(
        self,
        handler: AbstractExecutionHandler,
        input_data: Any,
        context: ExecutionContext,
    ) -> BaseExecutionOutput:
        """Execute a single step synchronously (runs in thread pool)."""
        start_time = time.time()

        try:
            # Validate input
            validated_input = handler.validate_input(input_data)

            # Execute (convert async to sync if needed)
            if asyncio.iscoroutinefunction(handler.execute):
                # Run async handler in thread's event loop
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    result = loop.run_until_complete(
                        handler.execute(validated_input, context)
                    )
                finally:
                    loop.close()
            else:
                result = handler.execute(validated_input, context)

            end_time = time.time()
            execution_time = int((end_time - start_time) * 1000)

            # Ensure result is BaseExecutionOutput and has execution time
            if isinstance(result, BaseExecutionOutput):
                result.execution_time_ms = execution_time
                return result
            else:
                # Wrap in BaseExecutionOutput if handler returned something else
                return BaseExecutionOutput(
                    success=True, result=result, execution_time_ms=execution_time
                )

        except Exception as e:
            end_time = time.time()
            execution_time = int((end_time - start_time) * 1000)

            logger.error(f"Handler execution failed: {str(e)}")

            return BaseExecutionOutput(
                success=False, error_message=str(e), execution_time_ms=execution_time
            )

    def _process_input_patterns(
        self, input_data: Any, step_outputs: Dict[int, BaseExecutionOutput]
    ) -> Any:
        """
        Process input data and replace output patterns like {{%%output_step_1%%}}.

        Args:
            input_data: The input data (could be any of the input models)
            step_outputs: Dictionary of completed step outputs

        Returns:
            Input data with patterns replaced
        """
        if not step_outputs:
            return input_data

        # Convert input to dict for processing
        if hasattr(input_data, "model_dump"):
            input_dict = input_data.model_dump()
        elif isinstance(input_data, dict):
            input_dict = input_data.copy()
        else:
            return input_data

        # Pattern to match {{%%output_step_N%%}}
        pattern = r"\{\{\%\%output_step_(\d+)\%\%\}\}"

        # Recursively process the dictionary
        processed_dict = self._replace_patterns_recursive(
            input_dict, pattern, step_outputs
        )

        # Convert back to original type if it was a Pydantic model
        if hasattr(input_data, "model_dump") and not isinstance(input_data, dict):
            try:
                # Use getattr to safely access model_validate
                model_validate_func = getattr(
                    input_data.__class__, "model_validate", None
                )
                if model_validate_func:
                    return model_validate_func(processed_dict)
            except Exception:
                # Fallback to processed dict if validation fails
                pass

        return processed_dict

    def _replace_patterns_recursive(
        self, data: Any, pattern: str, step_outputs: Dict[int, BaseExecutionOutput]
    ) -> Any:
        """Recursively replace patterns in nested data structures."""
        if isinstance(data, str):
            return self._replace_output_patterns(data, pattern, step_outputs)
        elif isinstance(data, dict):
            return {
                key: self._replace_patterns_recursive(value, pattern, step_outputs)
                for key, value in data.items()
            }
        elif isinstance(data, list):
            return [
                self._replace_patterns_recursive(item, pattern, step_outputs)
                for item in data
            ]
        else:
            return data

    def _replace_output_patterns(
        self, text: str, pattern: str, step_outputs: Dict[int, BaseExecutionOutput]
    ) -> str:
        """Replace output patterns in a text string."""

        def replace_match(match):
            step_id = int(match.group(1))
            if step_id in step_outputs:
                output = step_outputs[step_id]
                if output.success and output.result is not None:
                    # Convert result to string representation
                    if isinstance(output.result, str):
                        return output.result
                    elif hasattr(output.result, "model_dump_json"):
                        return output.result.model_dump_json()
                    else:
                        return str(output.result)
                else:
                    logger.warning(f"Referenced step {step_id} failed or has no result")
                    return f"[ERROR: Step {step_id} failed]"
            else:
                logger.warning(f"Referenced step {step_id} not found in outputs")
                return f"[ERROR: Step {step_id} not found]"

        return re.sub(pattern, replace_match, text)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - cleanup resources."""
        # Thread pool is managed by context manager in execute method
        pass
