from telegram import Update
from telegram.ext import ContextTypes


async def batch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 𝗕𝗔𝗧𝗖𝗛 𝗦𝗖𝗔𝗡\n\n"
        "Send your numbers, one per line.\n\n"
        "Example:\n"
        "+125455525585\n"
        "+2348071569915"
    )
