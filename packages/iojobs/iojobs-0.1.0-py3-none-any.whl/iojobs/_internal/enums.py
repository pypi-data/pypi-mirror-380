from enum import Enum


class ExecutionMode(str, Enum):
    MAIN = "main"
    THREAD = "thread"
    PROCESS = "process"


class JobStatus(str, Enum):
    SCHEDULED = "scheduled"
    CANCELED = "canceled"
    SUCCESS = "success"
    ERROR = "error"
