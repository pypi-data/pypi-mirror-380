"""
Execution state persistence manager.

This module handles saving and loading execution state to/from disk
to enable recovery from interruptions like power outages or server restarts.
"""

import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict, Any
import logging

from openagent.config.config import OpenAgentConfig
from openagent.models.scheduling import ExecutionPlan
from openagent.models.persistence import (
    ExecutionState,
    ExecutionPhase,
    PersistenceMetadata,
)
from openagent.core.execution_interfaces import BaseExecutionOutput

logger = logging.getLogger(__name__)


class PersistenceManager:
    """
    Manages execution state persistence to disk.

    Handles:
    - Saving/loading execution plans and state
    - Step-by-step progress tracking
    - Recovery from interruptions
    - Cleanup of old persistence files
    """

    def __init__(self, config: OpenAgentConfig):
        """Initialize persistence manager with configuration."""
        self.config = config
        self.output_folder = Path(config.execution_output_folder)
        self.enabled = config.execution_persistence_enabled

        if self.enabled:
            self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Create output directory structure if it doesn't exist."""
        try:
            self.output_folder.mkdir(parents=True, exist_ok=True)
            (self.output_folder / "states").mkdir(exist_ok=True)
            (self.output_folder / "plans").mkdir(exist_ok=True)
            (self.output_folder / "results").mkdir(exist_ok=True)
            (self.output_folder / "metadata").mkdir(exist_ok=True)
            logger.info(f"Persistence output directory ready: {self.output_folder}")
        except Exception as e:
            logger.error(f"Failed to create output directory: {str(e)}")
            self.enabled = False

    def create_new_execution(
        self, query: str, execution_plan: ExecutionPlan
    ) -> ExecutionState:
        """Create a new execution state using the ExecutionPlan's execution_id."""
        execution_id = execution_plan.execution_id

        execution_state = ExecutionState(
            execution_id=execution_id,
            phase=ExecutionPhase.PLANNING,
            original_query=query,
            execution_plan=(
                execution_plan.model_dump()
                if hasattr(execution_plan, "model_dump")
                else execution_plan.__dict__
            ),
            config_snapshot=(
                self.config.model_dump()
                if hasattr(self.config, "model_dump")
                else self.config.__dict__
            ),
        )

        # Get execution order
        try:
            execution_order, _ = execution_plan.get_execution_order()
            execution_state.execution_order = execution_order
        except Exception as e:
            logger.warning(f"Could not determine execution order: {str(e)}")

        if self.enabled:
            self._save_execution_plan(execution_id, execution_plan)
            self._save_execution_state(execution_state)

        return execution_state

    def save_execution_state(self, execution_state: ExecutionState):
        """Save execution state to disk."""
        if not self.enabled:
            return

        execution_state.update_timestamp()
        self._save_execution_state(execution_state)

    def _save_execution_state(self, execution_state: ExecutionState):
        """Internal method to save execution state."""
        try:
            state_file = (
                self.output_folder / "states" / f"{execution_state.execution_id}.json"
            )

            # Use model_dump with proper enum serialization
            state_data = execution_state.model_dump(mode="json")

            with open(state_file, "w") as f:
                json.dump(state_data, f, indent=2)

            # Save metadata
            self._save_metadata(execution_state.execution_id, "state", state_file)

            logger.debug(f"Saved execution state: {execution_state.execution_id}")

        except Exception as e:
            logger.error(
                f"Failed to save execution state {execution_state.execution_id}: {str(e)}"
            )

    def _save_execution_plan(self, execution_id: str, execution_plan: ExecutionPlan):
        """Save execution plan to disk."""
        try:
            plan_file = self.output_folder / "plans" / f"{execution_id}.json"

            plan_data = {
                "execution_id": execution_id,
                "created_at": datetime.now().isoformat(),
                "plan": (
                    execution_plan.model_dump()
                    if hasattr(execution_plan, "model_dump")
                    else execution_plan.__dict__
                ),
            }

            with open(plan_file, "w") as f:
                json.dump(plan_data, f, indent=2, default=str)

            # Save metadata
            self._save_metadata(execution_id, "plan", plan_file)

            logger.debug(f"Saved execution plan: {execution_id}")

        except Exception as e:
            logger.error(f"Failed to save execution plan {execution_id}: {str(e)}")

    def save_step_result(
        self, execution_id: str, step_id: int, result: BaseExecutionOutput
    ):
        """Save individual step result to disk."""
        if not self.enabled:
            return

        try:
            results_dir = self.output_folder / "results" / execution_id
            results_dir.mkdir(parents=True, exist_ok=True)

            result_file = results_dir / f"step_{step_id}.json"

            result_data = {
                "execution_id": execution_id,
                "step_id": step_id,
                "timestamp": datetime.now().isoformat(),
                "result": (
                    result.model_dump()
                    if hasattr(result, "model_dump")
                    else result.__dict__
                ),
            }

            with open(result_file, "w") as f:
                json.dump(result_data, f, indent=2, default=str)

            logger.debug(f"Saved step result: {execution_id}/step_{step_id}")

        except Exception as e:
            logger.error(
                f"Failed to save step result {execution_id}/step_{step_id}: {str(e)}"
            )

    def load_execution_state(self, execution_id: str) -> Optional[ExecutionState]:
        """Load execution state from disk."""
        if not self.enabled:
            return None

        try:
            state_file = self.output_folder / "states" / f"{execution_id}.json"

            if not state_file.exists():
                logger.debug(f"No state file found for execution: {execution_id}")
                return None

            with open(state_file, "r") as f:
                state_data = json.load(f)

            # Convert ISO datetime strings back to datetime objects
            for field in ["created_at", "updated_at", "started_at", "completed_at"]:
                if state_data.get(field):
                    state_data[field] = datetime.fromisoformat(state_data[field])

            # Convert step state datetimes
            for step_state in state_data.get("step_states", {}).values():
                for field in ["start_time", "end_time"]:
                    if step_state.get(field):
                        step_state[field] = datetime.fromisoformat(step_state[field])

            execution_state = ExecutionState.model_validate(state_data)
            logger.info(f"Loaded execution state: {execution_id}")
            return execution_state

        except Exception as e:
            logger.error(f"Failed to load execution state {execution_id}: {str(e)}")
            return None

    def load_execution_plan(self, execution_id: str) -> Optional[ExecutionPlan]:
        """Load execution plan from disk."""
        if not self.enabled:
            return None

        try:
            plan_file = self.output_folder / "plans" / f"{execution_id}.json"

            if not plan_file.exists():
                logger.debug(f"No plan file found for execution: {execution_id}")
                return None

            with open(plan_file, "r") as f:
                plan_data = json.load(f)

            # Reconstruct ExecutionPlan from saved data
            from openagent.models.scheduling import ExecutionPlan

            execution_plan = ExecutionPlan.model_validate(plan_data["plan"])

            logger.info(f"Loaded execution plan: {execution_id}")
            return execution_plan

        except Exception as e:
            logger.error(f"Failed to load execution plan {execution_id}: {str(e)}")
            return None

    def find_resumable_executions(self) -> List[ExecutionState]:
        """Find executions that can be resumed."""
        if not self.enabled:
            return []

        resumable_executions = []
        states_dir = self.output_folder / "states"

        if not states_dir.exists():
            return []

        try:
            for state_file in states_dir.glob("*.json"):
                execution_id = state_file.stem
                execution_state = self.load_execution_state(execution_id)

                if execution_state and execution_state.can_resume():
                    resumable_executions.append(execution_state)

            # Sort by last update time (most recent first)
            resumable_executions.sort(key=lambda x: x.updated_at, reverse=True)

            logger.info(f"Found {len(resumable_executions)} resumable executions")
            return resumable_executions

        except Exception as e:
            logger.error(f"Failed to find resumable executions: {str(e)}")
            return []

    def cleanup_old_files(self):
        """Clean up old persistence files based on config retention policy."""
        if not self.enabled:
            return

        try:
            cutoff_date = datetime.now() - timedelta(
                days=self.config.execution_state_cleanup_days
            )
            cleaned_count = 0

            for subdir in ["states", "plans", "results", "metadata"]:
                dir_path = self.output_folder / subdir
                if not dir_path.exists():
                    continue

                for file_path in dir_path.rglob("*.json"):
                    try:
                        file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                        if file_mtime < cutoff_date:
                            file_path.unlink()
                            cleaned_count += 1
                    except Exception as e:
                        logger.warning(f"Failed to clean up file {file_path}: {str(e)}")

            logger.info(f"Cleaned up {cleaned_count} old persistence files")

        except Exception as e:
            logger.error(f"Failed to cleanup old files: {str(e)}")

    def _save_metadata(self, execution_id: str, file_type: str, file_path: Path):
        """Save metadata for a persistence file."""
        try:
            metadata = PersistenceMetadata(
                execution_id=execution_id,
                file_type=file_type,
                file_size=file_path.stat().st_size if file_path.exists() else 0,
            )

            # Calculate checksum for integrity
            if file_path.exists():
                with open(file_path, "rb") as f:
                    metadata.checksum = hashlib.md5(f.read()).hexdigest()

            metadata_file = (
                self.output_folder / "metadata" / f"{execution_id}_{file_type}.json"
            )

            with open(metadata_file, "w") as f:
                json.dump(metadata.model_dump(), f, indent=2, default=str)

        except Exception as e:
            logger.warning(
                f"Failed to save metadata for {execution_id}_{file_type}: {str(e)}"
            )

    def get_execution_info(self, execution_id: str) -> Dict[str, Any]:
        """Get comprehensive information about an execution."""
        if not self.enabled:
            return {}

        info = {"execution_id": execution_id, "files": {}, "metadata": {}}

        # Check for state file
        state_file = self.output_folder / "states" / f"{execution_id}.json"
        info["files"]["state"] = state_file.exists()

        # Check for plan file
        plan_file = self.output_folder / "plans" / f"{execution_id}.json"
        info["files"]["plan"] = plan_file.exists()

        # Check for results directory
        results_dir = self.output_folder / "results" / execution_id
        if results_dir.exists():
            info["files"]["results"] = list(results_dir.glob("*.json"))
        else:
            info["files"]["results"] = []

        # Load metadata
        for file_type in ["state", "plan"]:
            metadata_file = (
                self.output_folder / "metadata" / f"{execution_id}_{file_type}.json"
            )
            if metadata_file.exists():
                try:
                    with open(metadata_file, "r") as f:
                        info["metadata"][file_type] = json.load(f)
                except Exception as e:
                    logger.warning(f"Failed to load metadata {metadata_file}: {str(e)}")

        return info

    def delete_execution_files(self, execution_id: str):
        """Delete all files related to an execution."""
        if not self.enabled:
            return

        try:
            deleted_count = 0

            # Delete state file
            state_file = self.output_folder / "states" / f"{execution_id}.json"
            if state_file.exists():
                state_file.unlink()
                deleted_count += 1

            # Delete plan file
            plan_file = self.output_folder / "plans" / f"{execution_id}.json"
            if plan_file.exists():
                plan_file.unlink()
                deleted_count += 1

            # Delete results directory
            results_dir = self.output_folder / "results" / execution_id
            if results_dir.exists():
                import shutil

                shutil.rmtree(results_dir)
                deleted_count += 1

            # Delete metadata files
            for file_type in ["state", "plan"]:
                metadata_file = (
                    self.output_folder / "metadata" / f"{execution_id}_{file_type}.json"
                )
                if metadata_file.exists():
                    metadata_file.unlink()
                    deleted_count += 1

            logger.info(f"Deleted {deleted_count} files for execution: {execution_id}")

        except Exception as e:
            logger.error(
                f"Failed to delete files for execution {execution_id}: {str(e)}"
            )

    def is_enabled(self) -> bool:
        """Check if persistence is enabled and working."""
        return self.enabled and self.output_folder.exists()
