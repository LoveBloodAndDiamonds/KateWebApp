import requests

from app.config import Config


async def send_telegram_message(message: str) -> bool:
    """
    Отправляет сообщение в Telegram чат.
    :param message: Текст сообщения для отправки.

    :return: bool: Возвращаем True, если сообщение было успешно отправлено, иначе False
    """
    try:
        url = f"https://api.telegram.org/bot{Config.BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": Config.TG_ADMIN_ID,
            "text": message
        }
        response = requests.post(url, data=payload)

        if not response.ok:
            raise Exception(f"Ошибка при отправке сообщения: {response.text}")

        return True

    except Exception as e:
        print(e)
        return False
