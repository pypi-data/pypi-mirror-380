from datetime import timedelta
from typing import List, Dict
from pydantic import BaseModel, Field


class RetryPolicy(BaseModel):
    initial_interval: int | None = None
    maximum_interval: int | None = None
    backoff_coefficient: float | None = None
    maximum_attempts: int | None = None
    non_retryable_error_types: List[str] | None = None


class Activity(BaseModel):
    name: str
    queue: str
    retry_policy: RetryPolicy | None = None
    schedule_to_close_timeout: int | None = None
    start_to_close_timeout: int | None = None
    heartbeat_timeout: int | None = None
    app_config: Dict = Field(default_factory=dict)


class Workflow(BaseModel):
    name: str
    id: str | None = None
    queue: str | None = None
    retry_policy: RetryPolicy | None = None
    execution_timeout: int | None = None
    run_timeout: int | None = None
    task_timeout: int | None = None
    app_config: Dict = Field(default_factory=dict)


class Executor(BaseModel):
    # workflow or activity config
    is_workflow: bool
    activity: Activity | None = None
    workflow: Workflow | None = None
    key_name: str | None = None  # Optional key name for identifying the executor
    input_keys: List[str] | None = None  # Optional key to extract specific input data
    wait_execution: bool = True  # Whether to wait for execution to complete


class InternalState(BaseModel):
    max_renews: int = 5
    current_renew: int = 0


class WorkflowInput(BaseModel):
    input: Dict
    workflow_start: Workflow
    executors: List[Executor] = Field(default_factory=list)
    internal_state: InternalState = Field(default_factory=InternalState)
    renew_when_expired: bool = False
    output_key: str | None = None  # Optional key to extract specific output data, if none return last executor output
