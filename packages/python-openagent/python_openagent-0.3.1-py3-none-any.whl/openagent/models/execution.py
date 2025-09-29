"""
Abstract base classes and interfaces for the OpenAgent execution engine.

This module defines the core interfaces that execution handlers must implement,
along with base classes for inputs and outputs.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, TypeVar, Generic, Optional, Union
from pydantic import BaseModel, Field, Json
from enum import Enum

# Type variables for generic typing
InputType = TypeVar("InputType", bound=BaseModel)
OutputType = TypeVar("OutputType", bound=BaseModel)


class ExecutionStatus(Enum):
    """Status of an execution step."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class BaseExecutionOutput(BaseModel):
    """Base class for all execution outputs.
    
    Attributes:
        success (bool): Whether the execution was successful.
        result (Optional[str]): The result of the execution, if any.
        error_message (Optional[str]): Error message if execution failed.
        execution_time_ms (int): Execution time in milliseconds.
    """

    success: bool = Field(..., description="Whether the execution was successful")
    result: Optional[str] = Field(None, description="The result of the execution")
    error_message: Optional[str] = Field(None, description="Error message if execution failed")
    execution_time_ms: int = Field(0, description="Execution time in milliseconds")
    
    def to_string(self) -> str:
        """Convert the output to a human-readable string."""
        raise NotImplementedError("to_string method must be implemented by subclasses")

class ExecutionContext(BaseModel):
    """Context passed to execution handlers."""

    step_id: int = Field(..., description="The step ID being executed")
    previous_outputs: Dict[int, BaseExecutionOutput] = Field(
        default_factory=dict, description="Outputs from previously executed steps"
    )
    config: Dict[str, Any] = Field(
        default_factory=dict, description="Configuration parameters"
    )


class AbstractExecutionHandler(ABC, Generic[InputType, OutputType]):
    """
    Abstract base class for all execution handlers.

    Each handler must implement the execute method to process inputs and return outputs.
    Handlers should be thread-safe and stateless for parallel execution.
    
    All handlers must return outputs that inherit from BaseExecutionOutput, which includes:
    - success: bool indicating whether execution was successful
    - result: Optional[str] with execution result summary  
    - error_message: Optional[str] with error details if execution failed
    - execution_time_ms: int with execution duration in milliseconds
    """

    @abstractmethod
    async def execute(
        self, input_data: InputType, context: ExecutionContext
    ) -> OutputType:
        """
        Execute the handler with the given input and context.

        Args:
            input_data: The input data for this execution step
            context: Execution context with previous outputs and configuration

        Returns:
            The output of the execution, which must inherit from BaseExecutionOutput
            and include success, result, error_message, and execution_time_ms fields

        Raises:
            ExecutionError: If the execution fails
        """
        pass

    @abstractmethod
    def get_input_type(self) -> type[InputType]:
        """Return the input type this handler expects."""
        pass

    @abstractmethod
    def get_output_type(self) -> type[OutputType]:
        """Return the output type this handler produces."""
        pass

    def validate_input(self, input_data: Any) -> InputType:
        """Validate and convert input data to the expected type."""
        input_type = self.get_input_type()
        if isinstance(input_data, input_type):
            return input_data
        elif isinstance(input_data, dict):
            return input_type.model_validate(input_data)
        else:
            raise ValueError(
                f"Invalid input type. Expected {input_type}, got {type(input_data)}"
            )


class ExecutionError(Exception):
    """Exception raised when execution fails."""

    def __init__(
        self,
        message: str,
        step_id: Optional[int] = None,
        original_error: Optional[Exception] = None,
    ):
        self.message = message
        self.step_id = step_id
        self.original_error = original_error
        super().__init__(message)


class ExecutionResult(BaseModel):
    """Result of an entire execution plan."""

    success: bool = Field(
        ..., description="Whether the entire execution was successful"
    )
    step_results: Dict[int, BaseExecutionOutput] = Field(
        default_factory=dict, description="Results from each step"
    )
    total_execution_time_ms: int = Field(default=0, description="Total execution time")
    failed_steps: list[int] = Field(
        default_factory=list, description="List of failed step IDs"
    )
    execution_order: list[int] = Field(
        default_factory=list, description="Order in which steps were executed"
    )
