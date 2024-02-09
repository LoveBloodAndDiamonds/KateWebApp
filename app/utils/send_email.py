from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib

from app.config import Config


async def send_email(message: str) -> bool:
    """
    Асинхронная отправка письма на электронную почту
    :param message: Текст сообщения
    :return: bool: Возвращаем True, если сообщение было успешно отправлено, иначе False
    """
    try:
        # Создание сообщения
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_LOGIN
        msg['To'] = Config.ACCEPTOR_EMAIL
        msg['Subject'] = 'Сообщение о похищении!'
        msg.attach(MIMEText(message, 'plain'))

        # Авторизация на почтовом сервере и отправка сообщения
        async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=465, use_tls=True) as server:
            await server.login(Config.EMAIL_LOGIN, Config.EMAIL_PASSWORD)
            await server.send_message(msg)

        return True
    except Exception as e:
        print(e)
        return False
