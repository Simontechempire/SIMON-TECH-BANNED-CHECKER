import os
import threading

from dotenv import load_dotenv
from flask import Flask
from telegram.ext import Application, CommandHandler

from database import init_db
from handlers.start import start
from handlers.scan import scan
from handlers.batch import batch
from handlers.report import report

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

app_web = Flask(__name__)


@app_web.route("/")
def home():
    return "SIMON BAN CHECKER is online ✅", 200


@app_web.route("/health")
def health():
    return "OK", 200


def run_web():
    app_web.run(
        host="0.0.0.0",
        port=PORT
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing from .env")

    init_db()

    threading.Thread(
        target=run_web,
        daemon=True
    ).start()

    bot = Application.builder().token(BOT_TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("scan", scan))
    bot.add_handler(CommandHandler("batch", batch))
    bot.add_handler(CommandHandler("report", report))

    print("🛡️ SIMON BAN CHECKER")
    print(f"🌐 Web server running on port {PORT}")
    print("🚀 Telegram bot is running...")

    bot.run_polling()


if __name__ == "__main__":
    main()
