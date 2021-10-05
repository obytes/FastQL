from decouple import config
from pydantic import BaseSettings

Key = config("SECRET_KEY")
queue = config("QUEUE")


class Settings((BaseSettings)):
    SECRET_KEY = Key
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@db/fastql"
    SQLALCHEMY_DATABASE_SSL = False
    SQLALCHEMY_DATABASE_MIN_POOL = 1
    SQLALCHEMY_DATABASE_MAX_POOL = 20


settings = Settings()
