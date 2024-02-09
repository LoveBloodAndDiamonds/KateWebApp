import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

from app.config import Config


async def send_email(data: dict) -> None:
    """
    Отправка письма на электронную почту
    :param data:  Словарь с данными из формы
    :return: None
    """
    # Авторизация на почтовом сервере
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(Config.EMAIL_LOGIN, Config.EMAIL_PASSWORD)

    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = Config.EMAIL_LOGIN
    msg['To'] = data["email"]
    msg['Subject'] = 'Сообщение о похищении!'

    # Создание текста сообщения
    body = f"""
    Имя:                    {data['name']} {data['surname']}
    Почта:                  {data['email']}
    Дата похищения:         {data['date']}
    Длительность похищения: {data['duration']}
    Кол-во похителей:       {data['number']}
    Описание похитителей:   {data['description']}
    Что похитители делали:  {data['experience']}
    Видел ли собаку?:       {data['saw_dog']}
    Доп. информация:        {data['additional']}

    """
    msg.attach(MIMEText(body, 'plain'))

    # Отправка сообщения
    server.send_message(msg)

    # Закрытие соединения с почтовым сервером
    server.quit()


data = {'name': 'zxc2', 'surname': 'zxc', 'email': 'ayaz2000@mail.ru', 'date': '2024-02-08', 'duration': 'asdasd',
        'number': 3, 'description': 'asd', 'experience': 'asd', 'saw_dog': True, 'additional': None}

asyncio.run(send_email(data))

