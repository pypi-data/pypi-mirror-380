import litellm
from typing import TypeVar, Type
from pydantic import BaseModel
from openagent.config import OpenAgentConfig

litellm.enable_json_schema_validation = True
T = TypeVar("T", bound=BaseModel)
config = OpenAgentConfig()


def gen_ai_resp_format(messages: list[dict[str, str]], resp_cast: Type[T]) -> T:
    model_response = (
        litellm.completion(
            model=config.gen_ai_model_name,
            api_key=config.gen_ai_api_key,
            api_version=config.gen_ai_api_version,
            base_url=config.gen_ai_api_endpoint,
            messages=messages,
            response_format=resp_cast,  # type: ignore
        )
        .choices[0]
        .message.content
    )  # type: ignore

    if model_response is None:
        raise ValueError("No response content received from the AI model")

    return resp_cast.model_validate_json(model_response)
