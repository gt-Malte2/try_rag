import importlib
import logging
import pathlib

from src.try_rag.config import settings
from src.try_rag.registry import run_task

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(name)s: %(message)s")


def load_tasks():
    tasks_dir = pathlib.Path(__file__).parent / "tasks"
    for path in tasks_dir.rglob("task.py"):
        module_name = ".".join(
            path.relative_to(pathlib.Path(__file__).parent).with_suffix("").parts
        )
        importlib.import_module(f"src.try_rag.{module_name}")


load_tasks()


def main():
    run_task(settings.BASE_TASK)


if __name__ == "__main__":
    main()
