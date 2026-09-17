import phonenumbers
from telegram import Update
from telegram.ext import ContextTypes

from database import save_check


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "🔎 𝗦𝗖𝗔𝗡 𝗡𝗨𝗠𝗕𝗘𝗥\n\n"
            "Use:\n"
            "/scan +2348071569915"
        )
        return

    phone = context.args[0].strip()

    try:
        number = phonenumbers.parse(phone, None)

        if not phonenumbers.is_valid_number(number):
            await update.message.reply_text(
                "❌ Invalid phone number."
            )
            return

        country = phonenumbers.region_code_for_number(number) or "Unknown"

        await update.message.reply_text(
            "🔎 𝗦𝗜𝗠𝗢𝗡 𝗡𝗨𝗠𝗕𝗘𝗥 𝗦𝗖𝗔𝗡\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📱 Number: {phone}\n"
            f"🌍 Country: {country}\n\n"
            "📡 Analyzing number...\n"
            "🛡️ Checking available status...\n\n"
            "⏳ Please wait..."
        )

        save_check(
            update.effective_user.id,
            phone,
            country,
            "Pending"
        )

    except phonenumbers.NumberParseException:
        await update.message.reply_text(
            "❌ Could not read that number.\n\n"
            "Example:\n"
            "/scan +2348071569915"
        )
