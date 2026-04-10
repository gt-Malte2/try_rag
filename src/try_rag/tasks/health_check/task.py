from src.try_rag.registry import task
from src.try_rag.tasks import TaskId

import logging

logger = logging.getLogger(__name__)


@task(TaskId.HEALTH_CHECK)
def health_check():
    logger.info("Everything healthy!")
