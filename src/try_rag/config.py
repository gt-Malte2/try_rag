from pydantic_settings import BaseSettings
from src.try_rag.tasks import TaskId


class Settings(BaseSettings):
    BASE_TASK: str

    class Config:
        env_file = ".env"

    @property
    def validated_base_task(self):
        valid_tasks = list(TaskId.__dict__.values())
        if self.BASE_TASK not in valid_tasks:
            raise ValueError(
                f"Invalid BASE_TASK: {self.BASE_TASK}. " f"Must be one of {valid_tasks}"
            )
        return self.BASE_TASK


settings = Settings()
