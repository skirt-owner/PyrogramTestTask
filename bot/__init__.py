import os


class Config:
    """
    Configuration class containing environment variable-based settings.

    :param api_id: The API ID.
    :type api_id: int

    :param api_hash: The API hash.
    :type api_hash: str

    :param postgres_username: The PostgreSQL username.
    :type postgres_username: str

    :param postgres_password: The PostgreSQL password.
    :type postgres_password: str

    :param postgres_host: The PostgreSQL host.
    :type postgres_host: str

    :param postgres_port: The PostgreSQL port.
    :type postgres_port: int

    :param postgres_database: The PostgreSQL database name.
    :type postgres_database: str
    """
    def __init__(
        self,
        api_id: int = int(os.getenv("API_ID")),
        api_hash: str = os.getenv("API_HASH"),
        postgres_username: str = os.getenv("POSTGRES_USERNAME"),
        postgres_password: str = os.getenv("POSTGRES_PASSWORD"),
        postgres_host: str = os.getenv("POSTGRES_HOST"),
        postgres_port: int = int(os.getenv("POSTGRES_PORT")),
        postgres_database: str = os.getenv("POSTGRES_DATABASE")
    ):
        self.api_id = api_id
        self.api_hash = api_hash
        self.postgres_username = postgres_username
        self.postgres_password = postgres_password
        self.postgres_host = postgres_host
        self.postgres_port = postgres_port
        self.postgres_database = postgres_database


config = Config()
