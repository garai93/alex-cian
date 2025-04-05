#!/bin/bash

echo "▶️ Установка браузеров Playwright..."
playwright install chromium

echo "🚀 Запускаем нейро-продавца..."
python telegram_sender.py
