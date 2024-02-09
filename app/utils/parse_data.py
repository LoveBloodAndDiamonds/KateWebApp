async def parse_data(data: dict) -> str:
    """
    Обрабатывает словарь, который собран из html формы и возвращает текст, который надо отправить в телеграме и email.
    :param data:
    :return:
    """
    return f"""
Имя: {data['name']} {data['surname']}
Почта: {data['email']}
Дата похищения: {data['date']}
Длительность похищения: {data['duration']}
Кол-во похителей: {data['number']}
Описание похитителей: {data['description']}
Что похитители делали: {data['experience']}
Видел ли собаку?: {data['saw_dog']}
Доп. информация: {data['additional']}
"""
