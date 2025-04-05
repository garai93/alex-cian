import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# Загружаем переменные из .env
load_dotenv()

# Читаем переменные окружения
api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")
recipient = os.getenv("TG_TARGET")  # Например: @ai_alex93

# Создаём клиент
client = TelegramClient('anon', api_id, api_hash)

def send_telegram_message(message):
    with client:
        client.send_message(recipient, message)

# Для теста (можно удалить потом)
if __name__ == "__main__":
    send_telegram_message("✅ Нейро-продавец успешно запущен на Railway!")
