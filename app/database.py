from typing import Dict, Any

import mysql.connector

from app.config import Config


class Database:

    def __init__(self) -> None:
        # Подключение к базе данных
        self.conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
        )
        # Создание курсора
        self.cursor = self.conn.cursor()

    def delete_database(self) -> None:
        """
        Функция удаляет базу данных.
        :return:
        """
        try:
            self.cursor.execute(f"DROP DATABASE IF EXISTS {Config.DB_DBNAME}")
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error while deleting database: {err}")

    def create_database(self) -> None:
        """
        Функция создает базу данных
        :return:
        """
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_DBNAME}")
        self.conn.database = Config.DB_DBNAME

    def create_table(self) -> None:
        """
        Функция создает таблицу в базе данных.
        """
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {Config.DB_DBNAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            surname VARCHAR(255),
            email VARCHAR(255),
            date DATE,
            duration VARCHAR(255),
            number INT,
            description TEXT,
            experience TEXT,
            saw_dog BOOLEAN,
            additional TEXT NULL
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, form_data: Dict[str, Any]) -> None:
        """
        Функция добавляет запись в таблицу.
        """
        insert_query = f"""
        INSERT INTO {Config.DB_DBNAME} (name, surname, email, date, duration, number, description, experience, saw_dog, additional)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, (
            form_data["name"],
            form_data["surname"],
            form_data["email"],
            form_data["date"],
            form_data["duration"],
            form_data["number"],
            form_data["description"],
            form_data["experience"],
            form_data["saw_dog"],
            form_data["additional"]
        ))
        self.conn.commit()

    def get_all(self):
        """
        Функция получает все данные из таблицы.
        :return:
        """
        q = f"SELECT * FROM {Config.DB_DBNAME}"
        self.cursor.execute(q)
        print(self.cursor.fetchall())

    def close(self) -> None:
        """
        Закрывает соединение с базой данных.
        """
        self.cursor.close()
        self.conn.close()
