import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ 𝗦𝗜𝗠𝗢𝗡 𝗕𝗔𝗡 𝗖𝗛𝗘𝗖𝗞𝗘𝗥\n\n"
        "Welcome to Simon Ban Checker.\n\n"
        "🔎 Use /scan to check a WhatsApp number\n"
        "📦 Use /batch for multiple numbers\n"
        "📋 Use /report for your history\n        "
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 𝗡𝗨𝗠𝗕𝗘𝗥 𝗦𝗖𝗔𝗡\n\n"
        "Send a WhatsApp number after the command.\n\n"
        "Example:\n"
        "/scan +2348071569915"
    )


async def batch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 𝗕𝗔𝗧𝗖𝗛 𝗦𝗖𝗔𝗡\n\n"
        "Send multiple WhatsApp numbers, one per line."
    )


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 𝗖𝗛𝗘𝗖𝗞 𝗥𝗘𝗣𝗢𝗥𝗧\n\n"
        "Your check history will appear here."
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing from .env")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("batch", batch))
    app.add_handler(CommandHandler("report", report))

    print("🛡️ Simon Ban Checker is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
