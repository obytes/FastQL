from decouple import config
from pydantic import BaseSettings

queue = config("QUEUE")


class Settings(((BaseSettings))):
    SECRET_KEY = config("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_SECONDS: int = config("ACCESS_TOKEN_EXPIRE_SECONDS", cast=int)
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")
    SQLALCHEMY_DATABASE_SSL = False
    SQLALCHEMY_DATABASE_MIN_POOL = 1
    SQLALCHEMY_DATABASE_MAX_POOL = 20


settings = Settings()
