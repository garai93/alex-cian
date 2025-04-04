
import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")
recipient = os.getenv("TG_TARGET")

client = TelegramClient('anon', api_id, api_hash)

def send_telegram_message(message):
    with client:
        client.send_message(recipient, message)
