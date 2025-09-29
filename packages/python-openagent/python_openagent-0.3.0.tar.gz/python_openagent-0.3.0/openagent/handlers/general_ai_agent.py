from typing import Any
import re
import asyncio

from openagent.models.execution import (
    AbstractExecutionHandler,
    ExecutionContext,
)
from openagent.models.scheduling import (
    GeneralAgentInput,
)

from openagent.models.handlers import (
    GeneralAgentOutput,
)

from openagent.core.llm import gen_ai_resp_format
from openagent.prompts.general_ai_agent import GeneralAIAgentPrompt

class GeneralAgentHandler(
    AbstractExecutionHandler[GeneralAgentInput, GeneralAgentOutput]
):
    """
    Handler for general AI agent tasks.
    This handler processes general queries using a language model.
    It takes a query as input and generates a response using the configured AI model.
    
    Attributes:
        input_type (type): The type of input this handler accepts (GeneralAgentInput).
        output_type (type): The type of output this handler produces (GeneralAgentOutput).
    
    Methods:
        get_input_type(): Returns the input type for this handler.
        get_output_type(): Returns the output type for this handler.
        execute(input_data, context): Executes the handler with the given input and context.
        sync_execute(input_data, context): Synchronous wrapper for execute method.
    
    Output Fields:
        success (bool): Whether the AI model execution was successful.
        result (str): Summary result from the AI model.
        response (str): Full response from the AI model.
        response_at (str): ISO timestamp when the response was generated.
        error_message (str, optional): Error message if execution failed.
        execution_time_ms (int): Time taken for the AI model to respond.
    
    Raises:
        ValueError: If the AI model does not return a valid response.
    """

    def get_input_type(self) -> type[GeneralAgentInput]:
        return GeneralAgentInput

    def get_output_type(self) -> type[GeneralAgentOutput]:
        return GeneralAgentOutput

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
    
    def _substitute_step_outputs(self, text: str, context: ExecutionContext) -> str:
        """
        Substitute placeholders in the format {%%output_step_x%%} with actual outputs from the context.
        Args:
            text (str): The input text containing placeholders.
            context (ExecutionContext): The execution context containing step outputs.
        Returns:
            str: The text with placeholders substituted by actual outputs.
        """
        pattern = r"\{\%\%output_step_(\d+)\%\%\}"
        
        def replace_match(match: re.Match) -> str:
            step_number = int(match.group(1))
            step_output = context.previous_outputs.get(step_number)
            return step_output if step_output is not None else match.group(0)
        
        return re.sub(pattern, replace_match, text)

    async def execute(
        self, input_data: GeneralAgentInput, context: ExecutionContext
    ) -> GeneralAgentOutput:
        """
        Execute the general AI agent handler.
        
        Args:
            input_data (GeneralAgentInput): The input data containing the query.
            context (ExecutionContext): The execution context.
        
        Returns:
            GeneralAgentOutput: The output containing:
                - success: Whether the execution was successful
                - result: Summary result from the AI model
                - response: Full response from the AI model
                - response_at: ISO timestamp of the response
                - error_message: Error message if execution failed (None on success)
                - execution_time_ms: Time taken for execution
        """
        query = self._substitute_step_outputs(input_data.query, context)
        prompt_template = GeneralAIAgentPrompt(query)
        return gen_ai_resp_format(messages=prompt_template.to_message_chain(), resp_cast=GeneralAgentOutput)

    
    def sync_execute(
        self, input_data: GeneralAgentInput, context: ExecutionContext
    ) -> GeneralAgentOutput:
        """
        Synchronous wrapper for the asynchronous execute method.
        
        Args:
            input_data (GeneralAgentInput): The input data containing the query.
            context (ExecutionContext): The execution context.
        
        Returns:
            GeneralAgentOutput: The output containing:
                - success: Whether the execution was successful
                - result: Summary result from the AI model
                - response: Full response from the AI model
                - response_at: ISO timestamp of the response
                - error_message: Error message if execution failed (None on success)
                - execution_time_ms: Time taken for execution
        """
        return asyncio.run(self.execute(input_data, context))