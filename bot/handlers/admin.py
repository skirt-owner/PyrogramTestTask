from pyrogram.types import Message

from bot.database.user import get_today_users
from bot.utils.custom_client import CustomClient


async def get_users_today_count(client: CustomClient, message: Message) -> None:
    """
    Get the count of users registered today and send the count as a message.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the command.
    :type message: Message

    :return: None    :rtype:
    """
    users = await get_today_users(client.session_marker)
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Today users count is {len(users)}"
    )
