"""
OpenAgent Core Module.

This module provides the core execution functionality including
execution planning, execution engine, and handler management.
"""

from typing import Optional
from .execution_plan import get_execution_plan, clear_plan_cache, get_plan_cache_stats
from .execution_engine import ExecutionEngine
from .execution_interfaces import (
    AbstractExecutionHandler,
    BaseExecutionOutput,
    ExecutionContext,
    ExecutionResult,
    ExecutionError,
)
from .placeholder_handlers import PLACEHOLDER_HANDLERS
from .persistence_manager import PersistenceManager
from ..models.persistence import ExecutionState, ExecutionPhase, StepState

from openagent.config.config import OpenAgentConfig
from openagent.models.scheduling import ExecutionHandler, ExecutionPlan

import logging

logger = logging.getLogger(__name__)


def create_production_engine(
    config: Optional[OpenAgentConfig] = None,
) -> ExecutionEngine:
    """
    Create a production-ready execution engine with all handlers registered.

    Args:
        config: OpenAgent configuration. If None, uses default config.

    Returns:
        Configured ExecutionEngine instance
    """
    if config is None:
        config = OpenAgentConfig()

    engine = ExecutionEngine(config)

    # Register all available handlers
    handler_mapping = {
        ExecutionHandler.WEB_SEARCH: PLACEHOLDER_HANDLERS["web_search"],
        ExecutionHandler.PYTHON_RUNTIME: PLACEHOLDER_HANDLERS["python_runtime"],
        ExecutionHandler.AGENT_POWERPOINT: PLACEHOLDER_HANDLERS["agent_powerpoint"],
        ExecutionHandler.AGENT_GENERAL: PLACEHOLDER_HANDLERS["agent_general"],
        ExecutionHandler.AGENT_EMAIL: PLACEHOLDER_HANDLERS["agent_email"],
        ExecutionHandler.AGENT_FILE_READER: PLACEHOLDER_HANDLERS["agent_file_reader"],
    }

    for handler_type, handler_instance in handler_mapping.items():
        engine.register_handler(handler_type, handler_instance)
        logger.info(f"Registered handler: {handler_type.value}")

    return engine


async def execute_query(query: str, config: Optional[OpenAgentConfig] = None):
    """
    End-to-end execution: Generate plan from query and execute it.

    This function demonstrates the complete workflow:
    1. Generate execution plan from natural language query
    2. Execute the plan using the execution engine
    3. Return the results

    Args:
        query: Natural language query
        config: OpenAgent configuration

    Returns:
        ExecutionResult with success status and step results
    """
    logger.info(f"Processing query: {query}")

    # Step 1: Generate execution plan
    try:
        execution_plan = get_execution_plan(query)
        logger.info(
            f"Generated execution plan with {execution_plan.total_entries} steps"
        )
    except Exception as e:
        logger.error(f"Failed to generate execution plan: {str(e)}")
        raise

    # Step 2: Create execution engine
    engine = create_production_engine(config)

    # Step 3: Execute the plan
    try:
        result = await engine.execute(execution_plan)
        logger.info(f"Execution completed. Success: {result.success}")
        return result
    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        raise


def get_available_handlers() -> list[str]:
    """Get list of available execution handler types."""
    return [handler.value for handler in ExecutionHandler]


def validate_execution_plan(plan: ExecutionPlan) -> dict:
    """
    Validate an execution plan for common issues.

    Returns:
        Dict with validation results
    """
    issues = []
    warnings = []

    # Check for circular dependencies
    try:
        execution_order, _ = plan.get_execution_order()
    except Exception as e:
        issues.append(f"Circular dependency detected: {str(e)}")
        execution_order = []

    # Check for missing dependencies
    step_ids = {entry.queue_position for entry in plan.entries}
    for entry in plan.entries:
        for dep in entry.dependency:
            if dep.dependency_index not in step_ids:
                issues.append(
                    f"Step {entry.queue_position} depends on non-existent step {dep.dependency_index}"
                )

    # Check for unused steps
    referenced_steps = set()
    for entry in plan.entries:
        for dep in entry.dependency:
            referenced_steps.add(dep.dependency_index)

    unreferenced_steps = (
        step_ids - referenced_steps - {min(step_ids) if step_ids else 0}
    )
    if unreferenced_steps:
        warnings.append(f"Steps not referenced by others: {list(unreferenced_steps)}")

    # Check for handler availability
    available_handlers = set(ExecutionHandler)
    required_handlers = {entry.execution_provider for entry in plan.entries}
    missing_handlers = required_handlers - available_handlers
    if missing_handlers:
        issues.append(
            f"Unknown execution handlers: {[h.value for h in missing_handlers]}"
        )

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
        "execution_order": execution_order,
        "total_steps": len(plan.entries),
        "parallel_opportunities": (
            len(step_ids) - len(execution_order) if execution_order else 0
        ),
    }


__all__ = [
    "get_execution_plan",
    "clear_plan_cache",
    "get_plan_cache_stats",
    "create_production_engine",
    "execute_query",
    "get_available_handlers",
    "validate_execution_plan",
    "ExecutionEngine",
    "ExecutionPlan",
    "AbstractExecutionHandler",
    "BaseExecutionOutput",
    "ExecutionContext",
    "ExecutionResult",
    "ExecutionError",
    "PLACEHOLDER_HANDLERS",
    "PersistenceManager",
    "ExecutionState",
    "ExecutionPhase",
    "StepState",
]
