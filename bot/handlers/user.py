from datetime import timedelta, datetime
from pyrogram.types import Message

from bot.database.user import get_user, add_user
from bot.utils.custom_client import CustomClient


async def funnel_1(client: CustomClient, message: Message) -> None:
    """
    Funnel 1 handler function.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the funnel.
    :type message: Message

    :return: None    :rtype:
    """
    await client.send_message(
        chat_id=message.chat.id,
        text="Добрый день!"
    )


async def funnel_2(client: CustomClient, message: Message) -> None:
    """
    Funnel 2 handler function.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the funnel.
    :type message: Message

    :return: None    :rtype:
    """
    await client.send_message(
        chat_id=message.chat.id,
        text="Подготовила для вас материал"
    )


async def funnel_3(client: CustomClient, message: Message) -> None:
    """
    Funnel 3 handler function.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the funnel.
    :type message: Message

    :return: None    :rtype:
    """
    await client.send_photo(
        chat_id=message.chat.id,
        photo="/Users/skirtowner/Documents/Projects/python/PyrogramTestTask/bot/utils/cat.jpeg"
    )


async def funnel_4(client: CustomClient, message: Message) -> None:
    """
    Funnel 4 handler function.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the funnel.
    :type message: Message

    :return: None    :rtype:
    """
    await client.send_message(
        chat_id=message.chat.id,
        text="Скоро вернусь с новым материалом!"
    )


async def register_user(client: CustomClient, message: Message) -> None:
    """
    Handler function to register a user and schedule the funnel.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the command.
    :type message: Message

    :return: None    :rtype:
    """
    # Check if the user already exists in the database
    user = await get_user(message.from_user.id, client.session_marker)
    if not user:
        # Register the user in the database
        await add_user(message.from_user.id, client.session_marker)

        client.scheduler.add_job(
            funnel_1,
            "date",
            run_date=datetime.now() + timedelta(minutes=10),
            id="funnel_1",
            args=[client, message]
        )
        client.scheduler.add_job(
            funnel_2,
            "date",
            run_date=datetime.now() + timedelta(seconds=5400),
            id="funnel_2",
            args=[client, message]
        )
        client.scheduler.add_job(
            funnel_3,
            "date",
            run_date=datetime.now() + timedelta(seconds=5405),
            id="funnel_3",
            args=[client, message]
        )
        client.scheduler.add_job(
            funnel_4,
            "date",
            run_date=datetime.now() + timedelta(hours=2),
            id="funnel_4",
            args=[client, message]
        )

        client.scheduler.start()


async def delete_last_message(client: CustomClient, message: Message) -> None:
    """
    Handler function to delete the job responsible for the last message in the funnel.

    :param client: CustomClient instance representing the bot client.
    :type client: CustomClient

    :param message: The incoming message object that triggered the command.
    :type message: Message

    :return: None    :rtype:
    """
    client.scheduler.remove_job('funnel_4')
