import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Config:
    # Токен телеграм бота
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    TG_ADMIN_ID: str = os.getenv("TG_ADMIN_ID")

    # Данные от почты
    EMAIL_LOGIN: str = os.getenv("EMAIL_LOGIN")
    EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")

    # email получателя
    ACCEPTOR_EMAIL: str = os.getenv("ACCEPTOR_EMAIL")

    # Данные базы данных
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_DBNAME: str = os.getenv("DB_DBNAME")

    # assert all([BOT_TOKEN, EMAIL_PASSWORD, EMAIL_LOGIN, DB_HOST, DB_USER, DB_PASSWORD, DB_DBNAME]), \
    #     "Вы не заполнили все данные в .env"
