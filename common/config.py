from os import environ
from tortoise import Tortoise

APP_ENV_LOCAL = "local"
APP_ENV_PROD = "prod"
APP_ENV = environ.get("API_ENV", "local")
IS_PRODUCTION = APP_ENV == APP_ENV_PROD
DB_URL: str = environ.get("DB_URL", f"sqlite:///database/sqlite_db/{APP_ENV}.db")

DB_CONFIG = {
    "connections": {
        # Dict format for connection
        # 'default': {
        #     'engine': 'tortoise.backends.asyncpg',
        #     'credentials': {
        #         'host': 'localhost',
        #         'port': '5432',
        #         'user': 'tortoise',
        #         'password': 'qwerty123',
        #         'database': 'test',
        #     }
        # },
        # Using a DB_URL string
        # 'default': DB_URL
        "default": "sqlite:///database/sqlite_db/local.db"
    },
    "apps": {
        "models": {
            "models": ["database.models.user_models", "aerich.models"],
            # If no default_connection specified, defaults to 'default'
            "default_connection": "default",
        }
    },
}


async def init():
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": ["database.models.user_models", "aerich.models"]},
    )
