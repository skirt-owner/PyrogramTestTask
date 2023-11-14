from datetime import datetime, timezone
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import select, Row
from typing import List, Union, Any, Sequence

from bot.database.models import User


async def add_user(user_id: int, async_session_maker: async_sessionmaker) -> None:
    """
    Add a new user to the database.

    :param user_id: The ID of the user to add.
    :type user_id: int

    :param async_session_maker: An asynchronous session maker object.
    :type async_session_maker: async_sessionmaker

    :raises SQLAlchemyError: If an error occurs during the database operation.
    """
    async with async_session_maker() as session:
        try:
            user = User(user_id=user_id)
            session.add(user)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e


async def get_user(user_id: int, async_session_maker: async_sessionmaker) -> Union[User, None]:
    """
    Retrieve a user from the database based on user ID.

    :param user_id: The ID of the user to retrieve.
    :type user_id: int

    :param async_session_maker: An asynchronous session maker object.
    :type async_session_maker: async_sessionmaker

    :return: The User object if found, None otherwise.
    :rtype: Union[User, None]

    :raises SQLAlchemyError: If an error occurs during the database operation.
    """
    async with async_session_maker() as session:
        try:
            user = await session.execute(select(User).filter_by(user_id=user_id))
            return user.first()
        except SQLAlchemyError as e:
            raise e


async def get_today_users(async_session_maker: async_sessionmaker) -> Sequence[Row[Any]]:
    """
    Retrieve all users created on the current date.

    :param async_session_maker: An asynchronous session maker object.
    :type async_session_maker: async_sessionmaker

    :return: A list of User objects created on the current date.
    :rtype: List[User]

    :raises SQLAlchemyError: If an error occurs during the database operation.
    """
    async with async_session_maker() as session:
        try:
            current_date = datetime.now(timezone.utc).date()
            users = await session.execute(select(User).where(User.creation_date >= current_date))
            return users.all()
        except SQLAlchemyError as e:
            raise e
