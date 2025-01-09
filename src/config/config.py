import os

DB_URL = os.getenv("DATABASE_URL", "sqlite:///telegram_task_bot.db")
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
