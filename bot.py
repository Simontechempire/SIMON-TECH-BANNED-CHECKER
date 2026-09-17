import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

from database import init_db
from handlers.start import start
from handlers.scan import scan
from handlers.batch import batch
from handlers.report import report

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing from .env")

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("batch", batch))
    app.add_handler(CommandHandler("report", report))

    print("🛡️ SIMON BAN CHECKER")
    print("🚀 Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
