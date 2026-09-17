from telegram import Update
from telegram.ext import ContextTypes

from database import get_history


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history = get_history(user_id)

    if not history:
        await update.message.reply_text(
            "📋 𝗠𝗬 𝗥𝗘𝗣𝗢𝗥𝗧𝗦\n\n"
            "You don't have any checks yet.\n\n"
            "Use /scan to check a number."
        )
        return

    text = "📋 𝗠𝗬 𝗥𝗘𝗣𝗢𝗥𝗧𝗦\n━━━━━━━━━━━━━━━━━━━━\n\n"

    for index, (phone, country, status, checked_at) in enumerate(
        history, start=1
    ):
        text += (
            f"{index}. 📱 {phone}\n"
            f"   🌍 {country}\n"
            f"   📊 {status}\n"
            f"   🕒 {checked_at}\n\n"
        )

    await update.message.reply_text(text)
