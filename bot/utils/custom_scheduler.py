from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger


class CustomScheduler(AsyncIOScheduler):
    """
    Customized AsyncIOScheduler class with additional features.

    :param kwargs: Additional keyword arguments to pass to the parent class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, *args, **kwargs):
        """
        Start the scheduler.

        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.

        :return: None        :rtype:
        """
        logger.info(f"Starting job")
        super().start(*args, **kwargs)
