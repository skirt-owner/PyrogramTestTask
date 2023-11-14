from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, func, BigInteger

from bot.database.base import Base


class User(Base):
    """
    Model representing a User in the application.

    :param user_id: The unique identifier of the user.
    :type user_id: int

    :param creation_date: The datetime when the user was created. Defaults to the current UTC datetime.
    :type creation_date: datetime

    :param update_date: The datetime when the user was last updated. Automatically updated on each update.
    :type update_date: datetime
    """

    __tablename__ = "pyrogram_users"

    user_id: int = Column(BigInteger, unique=True, nullable=False, primary_key=True)
    creation_date: datetime = Column(DateTime(timezone=True),
                                     default=datetime.now(tz=timezone.utc))
    update_date: datetime = Column(DateTime(timezone=True),
                                   onupdate=func.now(tz=timezone.utc))

    def __str__(self) -> str:
        """
        Return a string representation of the User object.

        :return: A string representation of the User object.
        :rtype: str
        """
        return f"<User:{self.user_id}>"

    def __repr__(self) -> str:
        """
        Return a string representation of the User object for debugging purposes.

        :return: A string representation of the User object.
        :rtype: str
        """
        return self.__str__()
