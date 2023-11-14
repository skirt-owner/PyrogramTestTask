import asyncio

from pyrogram.methods.utilities.idle import idle

from bot.database.base import Base
from bot.database.engine import create_database_url, create_async_engine, init_models, get_async_session_maker
from bot import config
from bot import handlers

from bot.utils.custom_client import CustomClient
from bot.utils.custom_scheduler import CustomScheduler


async def main() -> None:

    """
    Main entry point of the bot application.

    :return: None    :rtype:
    """
    database_url = create_database_url()
    async_engine = create_async_engine(database_url)
    await init_models(async_engine, Base.metadata)
    async_session_maker = get_async_session_maker(async_engine)

    scheduler = CustomScheduler()

    app = CustomClient(
        "personal_account",
        config.api_id,
        config.api_hash,
        async_session_maker,
        scheduler
    )

    await handlers.setup(app)

    await app.start()

    await idle()

    await app.stop()


if __name__ == '__main__':
    asyncio.run(main())
