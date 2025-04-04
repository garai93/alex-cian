
from playwright.sync_api import sync_playwright
import json
from telegram_sender import send_telegram_message

def check_cian_messages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = p.chromium.launch_persistent_context(
            user_data_dir="/tmp/cian_data",
            headless=True,
            storage_state="cian_state.json"
        )
        page = context.new_page()
        page.goto("https://www.cian.ru/my/messages/")
        page.wait_for_timeout(5000)

        # Пример: достаём все preview текста
        previews = page.locator(".message-preview__content").all_inner_texts()
        for msg in previews:
            send_telegram_message(f"📩 Новая заявка с ЦИАН: {msg}")

        browser.close()

if __name__ == "__main__":
    check_cian_messages()
