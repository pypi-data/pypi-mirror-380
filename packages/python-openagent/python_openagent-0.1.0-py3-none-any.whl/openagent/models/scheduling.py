from pydantic import BaseModel, Field
from enum import StrEnum

import networkx as nx
import json
import uuid
import hashlib
from typing import Optional


class ExecutionHandler(StrEnum):
    WEB_SEARCH = "web_search"
    PYTHON_RUNTIME = "python_runtime"
    AGENT_POWERPOINT = "agent_powerpoint"
    AGENT_GENERAL = "agent_general"
    AGENT_EMAIL = "agent_email"
    AGENT_FILE_READER = "agent_file_reader"


class DependencyType(StrEnum):
    OUTPUT = "output"
    ACTION = "action"


class Dependency(BaseModel):
    dependency_index: int
    dependency_type: DependencyType


class WebSearchInput(BaseModel):
    input_arg: str = Field(..., description="Short and concise query.")


class PythonRuntimeInput(BaseModel):
    dependencies: list[str] = Field(
        default_factory=list[str],
        description="List of dependencies in plaintext in pip style. e.g. `pandas>=2.2`",
    )
    code: str = Field(..., description="Python code to run")


class PowerpointAgentInput(BaseModel):
    content: str = Field(..., description="Content that should be in powerpoint")


class GeneralAgentInput(BaseModel):
    query: str


class EmailAgentInput(BaseModel):
    email_addrs: list[str]
    email_content: str


class FileReaderAgentInput(BaseModel):
    file_path: str = Field(..., description="Path to the file to read")


class ExecutionPlanEntry(BaseModel):
    queue_position: int = Field(..., description="First entry should start with 1.")
    dependency: list[Dependency] = Field(
        ..., description="Why this task depends on what."
    )
    execution_provider: ExecutionHandler
    input_info: (
        WebSearchInput
        | PythonRuntimeInput
        | PowerpointAgentInput
        | GeneralAgentInput
        | EmailAgentInput
        | FileReaderAgentInput
    )


class ExecutionPlan(BaseModel):
    entries: list[ExecutionPlanEntry]
    total_entries: int
    query: Optional[str] = Field(
        default=None, description="Original user query for hash-based execution_id"
    )
    execution_id: str = Field(
        default="",
        description="Execution identifier - auto-generated from query hash or UUID",
    )

    def __init__(self, **data):
        """Initialize ExecutionPlan with automatic execution_id generation."""
        query = data.get("query")

        # Always use query-based hash if query is provided, regardless of existing execution_id
        if query:
            # Generate deterministic hash-based ID from query
            query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()[:16]
            data["execution_id"] = f"query-{query_hash}"
        elif not data.get("execution_id"):
            # Only fallback to UUID if no query AND no execution_id provided
            data["execution_id"] = str(uuid.uuid4())

        super().__init__(**data)

    def get_execution_order(self) -> tuple[list[int], nx.DiGraph]:
        """Return execution order using topological sort."""
        G = nx.DiGraph()
        for entry in self.entries:
            G.add_node(entry.queue_position)
            for dep in entry.dependency:
                G.add_edge(dep.dependency_index, entry.queue_position)
        order = list(nx.topological_sort(G))
        return order, G

    def to_json(self, file_path: str, indent: int = 4) -> None:
        """Save execution plan to json file."""
        with open(file_path, "w") as f:
            json.dump(self.model_dump(), f, indent=indent)
