# create a poe task that does the postprocessing
from src.try_rag.registry import task
from src.try_rag.tasks import TaskId


@task(TaskId.POSTPROCESS)
def postprocess():
    pass
