"""
Стартовая точка программы.
Запуск происходит через консоль: uvicorn app.__main__:app --reload
"""

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from app.database import Database

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

database = Database()  # Создание обьекта который управляет бд
database.delete_database()  # Удаление старой базы данных каждый раз на запуске
database.create_database()  # Создание базы данных
database.create_table()  # Создание таблицы в базе данных
database.get_all()  # todo


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit-form")
async def handle_form(
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

    database.insert_data(form_data)
    return  # todo return confirm page
