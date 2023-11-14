from typing import Union, Optional

from loguru import logger
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, Message

from bot.utils.custom_scheduler import CustomScheduler


class CustomClient(Client):
    """
    Customized Pyrogram Client class with additional features.

    :param session_name: The name of the session.
    :type session_name: str

    :param api_id: The API ID of the bot.
    :type api_id: int

    :param api_hash: The API hash of the bot.
    :type api_hash: str

    :param session_marker: The session marker for database operations.
    :type session_marker: SessionMarker

    :param scheduler: The scheduler for task/job management.
    :type scheduler: Scheduler

    :param kwargs: Additional keyword arguments to pass to the parent class.
    """

    def __init__(
        self,
        session_name: str,
        api_id: int,
        api_hash: str,
        session_marker,
        scheduler: CustomScheduler,
        **kwargs
    ):
        super().__init__(session_name, api_id, api_hash, **kwargs)
        self.session_marker = session_marker
        self.scheduler = scheduler

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        *args,
        **kwargs
    ) -> Message:
        """
        Send a message to a chat.

        :param chat_id: The ID or username of the chat to send the message to.
        :type chat_id: Union[int, str]

        :param text: The text of the message.
        :type text: str

        :param reply_markup: Inline keyboard markup for the message. Defaults to None.
        :type reply_markup: Optional[InlineKeyboardMarkup]

        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.

        :return: The sent message object.
        :rtype: Message
        """
        logger.info(f"Sending message: {args} {kwargs}")
        return await super().send_message(chat_id, text, reply_markup=reply_markup, *args, **kwargs)
