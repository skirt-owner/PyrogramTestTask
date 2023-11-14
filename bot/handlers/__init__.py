from typing import List

from pyrogram import filters
from pyrogram.handlers import MessageHandler

from bot.handlers.user import register_user, delete_last_message
from bot.handlers.admin import get_users_today_count
from bot.utils.custom_client import CustomClient


async def setup(app: CustomClient) -> None:
    """
    Set up the event handlers for the bot application.

    :param app: The bot application instance.
    :type app: AppType

    :return: None    :rtype:
    """
    app.add_handler(MessageHandler(register_user, ~filters.me & filters.private & filters.incoming))
    app.add_handler(MessageHandler(delete_last_message, filters.outgoing & filters.regex("Хорошего дня")))
    app.add_handler(MessageHandler(get_users_today_count, filters.chat("self") & filters.command("users_today")))


__all__: List[str] = ["setup"]
