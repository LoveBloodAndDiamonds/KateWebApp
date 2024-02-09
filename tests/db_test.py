from app.database import Database


database = Database()  # Создание обьекта который управляет бд
database.delete_database()  # Удаление старой базы данных каждый раз на запуске
database.create_database()  # Создание базы данных
database.create_table()  # Создание таблицы в базе данных
database.get_all()  # todo


form_data = {
        "name": "1",
        "surname": "surname",
        "email": "email",
        "date": "date",
        "duration": "duration",
        "number": 123,
        "description": "description",
        "experience": "experience",
        "saw_dog": True if "saw_dog" == 'yes' else False,
        "additional": "additional"
    }

database.insert_data(form_data)
database.get_all()
