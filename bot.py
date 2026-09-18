import os
import threading

from dotenv import load_dotenv
from flask import Flask
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from database import init_db
from handlers.start import start
from handlers.scan import scan
from handlers.batch import batch
from handlers.report import report
from handlers.buttons import button_handler


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))


# ═══════════════════════════════════════
# 🌐 WEB SERVER FOR RENDER
# ═══════════════════════════════════════

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "🛡️ SIMON BAN CHECKER — ONLINE ✅", 200


@web_app.route("/health")
def health():
    return "OK", 200


def run_web():
    web_app.run(
        host="0.0.0.0",
        port=PORT
    )


# ═══════════════════════════════════════
# 🤖 TELEGRAM BOT
# ═══════════════════════════════════════

def main():

    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing from .env"
        )

    # Initialize database
    init_db()

    # Start web server
    threading.Thread(
        target=run_web,
        daemon=True
    ).start()

    # Create Telegram application
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # ═══════════════════════════════════
    # 📌 COMMANDS
    # ═══════════════════════════════════

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("scan", scan)
    )

    application.add_handler(
        CommandHandler("batch", batch)
    )

    application.add_handler(
        CommandHandler("report", report)
    )

    # ═══════════════════════════════════
    # 🔘 INLINE BUTTONS
    # ═══════════════════════════════════

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🛡️ SIMON BAN CHECKER")
    print("🌐 Web server: ONLINE")
    print("🤖 Telegram bot: ONLINE")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Start bot
    application.run_polling()


# ═══════════════════════════════════════
# 🚀 START
# ═══════════════════════════════════════

if __name__ == "__main__":
    main()
