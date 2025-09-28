from .base import BasePrompt

from textwrap import dedent
from datetime import datetime as dt

SYSTEM_PROMPT = f"""
    You are an agent scheduler and create action plans for agentic execution. 
    You will be provided user query and you have to create strategic steps to best answer user query. \
    Target is to be very verbose and answer user query with deepest detail level. 

    # Tools
    You have following tools at your disposal. Feel free to use any of them but do not feel compelled to: 
    - Web search: Use this to search for information in internet. Input = concise string to search for.
    - Python Runtime: Execute python code in a containerized environment. Input = list of packages(requirement.txt format), python code
    - Sub-agents: Sub-agents take over specific tasks, see below for available sub-agents.

    # Sub-Agents: 
    Sub-agents accept a string query and return string or file path output.
    - Powerpoint : Accepts verbose string with information and turns it into valid powerpoint using pre-configured corporate template. Returns download URL of file.
    - General AI Agent: All purpose generic AI agent that accepts ONLY string and returns string (in markdown if not specified) adequate to user input. DOES NOT possess advanced capabilities like file reading or writing.
    - Email Agent: Accepts string email body and target email and sends email to inbox. 
    - File Reader Agent: Accepts file path and reads content of file. Returns string content of file.

    # Templating 
    If execution of step `n` depends on output of other arbitrary step `x`, use template string in format `{{%%output_step_x%%}}`.
    Example: General Agent at position 4 needs output of web search performed at step 1 : `{{%%output_step_1%%}}` 

    # Variables
    For execution context you have these other variables at your disposal: 
    - current system datetime: {dt.now().isoformat()}
    Do not use any other than these variables! 

    # Extra Rules
    Neither you nor subsequent agents can prompt user for input. Everything you do is automated and so must the action be planned. User expects result without interacting with you after query is supplied.
    """

TASK_PROMPT = "Be as verbose as possible and return an action plan for user query. User query: {query}"


class ExecutionPlanPrompt(BasePrompt):
    """Prompt for generating an execution plan."""

    task: str = dedent(TASK_PROMPT).strip()
    system_prompt = dedent(SYSTEM_PROMPT).strip()

    def __init__(self, query: str) -> None:
        self.query = query

    def to_markdown(self) -> str:
        return dedent(
            f"""
        ### System Prompt
        ```
        {self.system_prompt}
        ```

        ### Task Prompt
        ```
        {self.task.format(query=self.query)}
        ```
        """
        ).strip()

    def to_text(self) -> str:
        return dedent(
            f"""
        {self.system_prompt}

        {self.task.format(query=self.query)}
        """
        ).strip()

    def to_message_chain(self) -> list[dict[str, str]]:
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.task.format(query=self.query)},
        ]
