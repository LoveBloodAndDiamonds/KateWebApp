"""
Стартовая точка программы.
Запуск происходит через консоль: uvicorn app.__main__:app --reload
"""

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from app.database import Database
from app.utils import send_email, send_telegram_message, parse_data

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

database = Database()  # Создание обьекта который управляет бд
database.delete_database()  # Удаление старой базы данных каждый раз на запуске
database.create_database()  # Создание базы данных
database.create_table()  # Создание таблицы в базе данных


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit-form")
async def handle_form(
        request: Request,
        name: str = Form(...),
        surname: str = Form(...),
        email: str = Form(...),
        date: str = Form(...),
        duration: str = Form(...),
        number: int = Form(...),
        description: str = Form(...),
        experience: str = Form(...),
        saw_dog: str = Form(...),
        additional: str = Form(None)
):
    form_data = {
        "name": name,
        "surname": surname,
        "email": email,
        "date": date,
        "duration": duration,
        "number": number,
        "description": description,
        "experience": experience,
        "saw_dog": True if saw_dog == 'yes' else False,
        "additional": additional
    }

    database.insert_data(form_data)  # Добавляем запись в бд

    message: str = await parse_data(form_data)  # Конструируем сообщение из полученных данных
    email_result: bool = await send_email(message)  # Отправлять сообщение email
    telegram_result: bool = await send_telegram_message(message)  # Отправляем сообщение telegram

    # Возвращаем пользователем шаблон с подтверждением о том, что заявка обработана.
    return templates.TemplateResponse("report.html", {
        "request": request,
        "date": date,
        "duration": duration,
        "description": description,
        "saw_dog": "Да" if saw_dog == 'yes' else "Нет",
        "email": email,
        "email_result": "Да" if email_result else "Нет",
        "telegram_result": "Да" if telegram_result else "Нет"
    })
