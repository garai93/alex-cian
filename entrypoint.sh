#!/bin/bash

echo "▶️ Устанавливаем Playwright браузеры..."
playwright install chromium

echo "🚀 Запускаем парсинг ЦИАН и отправку в Telegram..."
python cian_checker.py
