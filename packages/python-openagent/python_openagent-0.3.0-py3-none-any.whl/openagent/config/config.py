from pydantic_settings import BaseSettings
from pydantic import Field


class OpenAgentConfig(BaseSettings):
    # GenAI Configuration
    gen_ai_api_endpoint: str = Field(default="", alias="GEN_AI_API_ENDPOINT")
    gen_ai_api_key: str = Field(default="", alias="GEN_AI_API_KEY")
    gen_ai_api_version: str = Field(default="", alias="GEN_AI_API_VERSION")
    gen_ai_model_name: str = Field(default="", alias="GEN_AI_MODEL_NAME")

    # Execution Engine Configuration
    execution_max_workers: int = Field(
        default=4,
        alias="EXECUTION_MAX_WORKERS",
        description="Maximum number of worker threads for parallel execution",
    )
    execution_step_timeout: int = Field(
        default=300,
        alias="EXECUTION_STEP_TIMEOUT",
        description="Timeout for individual execution steps in seconds",
    )
    execution_fail_fast: bool = Field(
        default=True,
        alias="EXECUTION_FAIL_FAST",
        description="Whether to stop execution immediately on first failure",
    )
    execution_retry_attempts: int = Field(
        default=3,
        alias="EXECUTION_RETRY_ATTEMPTS",
        description="Number of retry attempts for failed steps",
    )
    execution_retry_delay: float = Field(
        default=1.0,
        alias="EXECUTION_RETRY_DELAY",
        description="Delay between retry attempts in seconds",
    )

    # Execution Persistence Configuration
    execution_persistence_enabled: bool = Field(
        default=True,
        alias="EXECUTION_PERSISTENCE_ENABLED",
        description="Enable execution state persistence for recovery",
    )
    execution_output_folder: str = Field(
        default="./execution_output",
        alias="EXECUTION_OUTPUT_FOLDER",
        description="Folder to store execution state and output files",
    )
    execution_state_cleanup_days: int = Field(
        default=7,
        alias="EXECUTION_STATE_CLEANUP_DAYS",
        description="Number of days to keep old execution state files",
    )
    execution_auto_resume: bool = Field(
        default=True,
        alias="EXECUTION_AUTO_RESUME",
        description="Automatically resume interrupted executions on restart",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
