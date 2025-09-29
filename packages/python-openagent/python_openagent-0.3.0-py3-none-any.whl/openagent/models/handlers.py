from openagent.models.execution import BaseExecutionOutput
from typing import Any
from pydantic import Field
from datetime import datetime as dt, timezone as tz

class WebSearchOutput(BaseExecutionOutput):
    """Output model for web search operations.
    
    Inherits success, result, error_message, and execution_time_ms from BaseExecutionOutput.
    
    Attributes:
        search_results (list[dict[str, Any]]): List of search results.
        query (str): The search query that was executed.
        results_count (int): Number of search results returned.
    """

    search_results: list[dict[str, Any]] = []
    query: str = ""
    results_count: int = 0

    def to_string(self) -> str:
        # stringfy search results in readable format
        result_str = f"Search Query: {self.query}\nResults Count: {self.results_count}\n"
        for i, result in enumerate(self.search_results):
            result_str += f"\nResult {i+1}:\n"
            for key, value in result.items():
                result_str += f"  {key}: {value}\n"
        return result_str

class PythonRuntimeOutput(BaseExecutionOutput):
    """Output model for Python runtime operations.
    
    Inherits success, result, error_message, and execution_time_ms from BaseExecutionOutput.
    
    Attributes:
        stdout (str): Standard output from the Python execution.
        stderr (str): Standard error from the Python execution.
        return_code (int): Exit code from the Python execution.
        variables (dict[str, Any]): Variables captured from the execution context.
    """

    stdout: str = ""
    stderr: str = ""
    return_code: int = 0
    variables: dict[str, Any] = {}

    def to_string(self) -> str:
        return (
            f"Return Code: {self.return_code}\n"
            f"STDOUT:\n{self.stdout}\n"
            f"STDERR:\n{self.stderr}\n"
            f"Variables: {self.variables}\n"
        )


class PowerpointAgentOutput(BaseExecutionOutput):
    """Output model for PowerPoint agent operations.
    
    Inherits success, result, error_message, and execution_time_ms from BaseExecutionOutput.
    
    Attributes:
        file_path (str): Path to the generated PowerPoint file.
        slide_count (int): Number of slides in the presentation.
        content_summary (str): Summary of the presentation content.
    """

    file_path: str = ""
    slide_count: int = 0
    content_summary: str = ""

    def to_string(self) -> str:
        return (
            f"File Path: {self.file_path}\n"
            f"Slide Count: {self.slide_count}\n"
            f"Content Summary: {self.content_summary}\n"
        )


class GeneralAgentOutput(BaseExecutionOutput):
    """Output model for general agent operations.
    
    Inherits success, result, error_message, and execution_time_ms from BaseExecutionOutput.
    
    Attributes:
        response (str): The agent's response to the query.
        response_at (str): ISO timestamp when the response was generated.
    """

    response: str = ""
    response_at: str = Field(default_factory=lambda: dt.now(tz.utc).isoformat())

    def to_string(self) -> str:
        return (
            f"Response:\n{self.response}\n"
            f"Response ISO Timestamp: {self.response_at}\n"
        )


class EmailAgentOutput(BaseExecutionOutput):
    """Output model for email agent operations.
    
    Inherits success, result, error_message, and execution_time_ms from BaseExecutionOutput.
    
    Attributes:
        sent_count (int): Number of emails successfully sent.
        failed_addresses (list[str]): List of email addresses that failed to receive the email.
        message_id (str): Unique identifier for the sent message.
    """

    sent_count: int = 0
    failed_addresses: list[str] = []
    message_id: str = ""

    def to_string(self) -> str:
        return (
            f"Sent Count: {self.sent_count}\n"
            f"Failed Addresses: {', '.join(self.failed_addresses)}\n"
            f"Message ID: {self.message_id}\n"
        )


class FileReaderAgentOutput(BaseExecutionOutput):
    """Output model for file reading operations.
    
    Inherits success, result, error_message, and execution_time_ms from BaseExecutionOutput.
    
    Attributes:
        file_content (str): Content of the file that was read.
        file_size (int): Size of the file in bytes.
        file_type (str): Type/extension of the file.
        metadata (dict[str, Any]): Additional metadata about the file or read operation.
    """

    file_content: str = ""
    file_size: int = 0
    file_type: str = ""
    metadata: dict[str, Any] = {}

    def to_string(self) -> str:
        return (
            f"File Content: {self.file_content}\n"
            f"File Size: {self.file_size}\n"
            f"File Type: {self.file_type}\n"
            f"Metadata: {self.metadata}\n"
        )
