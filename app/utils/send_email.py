from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

from app.config import Config


async def send_email(message: str) -> bool:
    """
    Отправка письма на электронную почту
    :param message: Текст сообщения
    :return: bool: Возвращаем True, если сообщение было успешно отправлено, иначе False
    """
    try:
        # Авторизация на почтовом сервере
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(Config.EMAIL_LOGIN, Config.EMAIL_PASSWORD)

        # Создание сообщения
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_LOGIN
        msg['To'] = Config.ACCEPTOR_EMAIL
        msg['Subject'] = 'Сообщение о похищении!'

        msg.attach(MIMEText(message, 'plain'))

        # Отправка сообщения
        server.send_message(msg)

        # Закрытие соединения с почтовым сервером
        server.quit()

        return True
    except Exception as e:
        print(e)
        return False
