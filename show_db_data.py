"""
Модуль при запуске позволяет посмотреть, какие данные уже есть в базе данных.
"""

from app.database import Database


database = Database()  # Создание обьекта который управляет бд
database.create_database()  # Создание базы данных
database.create_table()  # Создание таблицы в базе данных
res = database.get_all()

for r in res:
    print(r)
