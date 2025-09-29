from openagent.prompts.base import BasePrompt

from textwrap import dedent
from datetime import datetime as dt

SYSTEM_PROMPT = """
    You are a General AI Agent that can perform a variety of tasks based on agent input.
    You are an sub agent of a larger multi-agent system and work in an automated fashion.
    You accept ONLY string input and return string output (in markdown if not specified)
    adequate to agent input. You DO NOT possess advanced capabilities like file reading or
    writing. 
    
    You are not allowed to prompt user for input. Everything you do is automated
    and so must the action be planned. User expects result without interacting with you after
    query is supplied. 
    
    You have access to the current system datetime: {current_iso_time}.
    You have no other access to external information or APIs. Only raw LLM capabilities.
    """

TASK_PROMPT = """
    Below is the query you have to respond to. Follow the instructions precisely.
    ---
    Query: {query}
    ---
    """


class GeneralAIAgentPrompt(BasePrompt):
    """Prompt for generating an general all purpose AI response."""

    task: str = dedent(TASK_PROMPT).strip()
    system_prompt = dedent(SYSTEM_PROMPT).strip()

    def __init__(self, query: str) -> None:
        self.query = query

    @property
    def parametrized_sys_prompt(self) -> str:
        return self.system_prompt.format(current_iso_time=dt.now().isoformat())

    @property
    def parametrized_task_prompt(self) -> str:
        return self.task.format(query=self.query)

    def to_markdown(self) -> str:
        return dedent(
            f"""
        ### System Prompt
        ```
        {self.parametrized_sys_prompt}
        ```

        ### Task Prompt
        ```
        {self.parametrized_task_prompt}
        ```
        """
        ).strip()

    def to_text(self) -> str:
        return dedent(
            f"""
        {self.parametrized_sys_prompt}

        {self.parametrized_task_prompt}
        """
        ).strip()

    def to_message_chain(self) -> list[dict[str, str]]:
        return [
            {"role": "system", "content": self.parametrized_sys_prompt},
            {"role": "user", "content": self.parametrized_task_prompt},
        ]
