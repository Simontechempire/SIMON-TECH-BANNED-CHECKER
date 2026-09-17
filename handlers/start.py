from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from database import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(
        user.id,
        user.username,
        user.first_name
    )

    keyboard = [
        [
            InlineKeyboardButton("🔎 Scan Number", callback_data="scan"),
            InlineKeyboardButton("📦 Batch Scan", callback_data="batch"),
        ],
        [
            InlineKeyboardButton("📋 My Reports", callback_data="reports"),
            InlineKeyboardButton("🌍 Country", callback_data="country"),
        ],
        [
            InlineKeyboardButton("❓ Guide", callback_data="guide"),
            InlineKeyboardButton("📢 Updates", callback_data="updates"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "🛡️ 𝗦𝗜𝗠𝗢𝗡 𝗕𝗔𝗡 𝗖𝗛𝗘𝗖𝗞𝗘𝗥\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👋 Welcome, {user.first_name}!\n\n"
        "Check available WhatsApp account-status "
        "information using our checker.\n\n"
        "🔎 /scan — Check a number\n"
        "📦 /batch — Check multiple numbers\n"
        "📋 /report — View your reports\n"
        "🌍 /region — Country settings\n"
        "⚙️ /service — Service status\n"
        "❓ /guide — How it works\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚡ 𝗦𝗶𝗺𝗼𝗻 𝗧𝗲𝗰𝗵"
    )

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )
