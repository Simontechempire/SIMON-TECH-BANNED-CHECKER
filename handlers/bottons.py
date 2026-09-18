from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


CHANNEL_URL = "https://t.me/babyupdategc"


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    if query.data == "check":

        keyboard = [
            [
                InlineKeyboardButton(
                    "❌ Cancel",
                    callback_data="cancel"
                )
            ]
        ]

        await query.edit_message_text(
            "🔎 𝗖𝗛𝗘𝗖𝗞 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "📱 Send the WhatsApp phone number.\n\n"
            "Example:\n"
            "+2348071569915\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "⏳ Waiting for number...",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        context.user_data["waiting_for_number"] = True

    elif query.data == "bulk":

        await query.edit_message_text(
            "📦 𝗕𝗨𝗟𝗞 𝗖𝗛𝗘𝗖𝗞\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Send multiple numbers, one per line.\n\n"
            "Example:\n"
            "+2348071569915\n"
            "+125455525585\n\n"
            "⏳ Waiting for numbers..."
        )

        context.user_data["waiting_for_bulk"] = True

    elif query.data == "history":

        await query.edit_message_text(
            "📜 𝗠𝗬 𝗛𝗜𝗦𝗧𝗢𝗥𝗬\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Your previous checks will appear here.\n\n"
            "Use the menu to start a new check."
        )

    elif query.data == "help":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔎 Start Checking",
                    callback_data="check"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 Back",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            "📖 𝗛𝗢𝗪 𝗜𝗧 𝗪𝗢𝗥𝗞𝗦\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "1️⃣ Tap 🔎 Start Checking\n"
            "2️⃣ Send a phone number\n"
            "3️⃣ The bot analyzes the available information\n"
            "4️⃣ Your result is displayed\n\n"
            "📱 Use international format.\n"
            "Example: +2348071569915",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "guest":

        await query.edit_message_text(
            "👤 𝗚𝗨𝗘𝗦𝗧 𝗠𝗢𝗗𝗘\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "You are currently using Guest Mode.\n\n"
            "🔎 Basic number checking is available.\n"
            "📜 History may require an account."
        )

    elif query.data == "language":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🇬🇧 English",
                    callback_data="language_en"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 Back",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            "🌍 𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘\n\n"
            "Choose your preferred language:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "language_en":

        await query.answer("🇬🇧 English selected")

        await query.edit_message_text(
            "🌍 𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘\n\n"
            "🇬🇧 English is now selected."
        )

    elif query.data == "news":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📢 Subscribe to Channel",
                    url=CHANNEL_URL
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 Back to Menu",
                    callback_data="home"
                )
            ]
        ]

        await query.edit_message_text(
            "📢 𝗦𝗜𝗠𝗢𝗡 𝗧𝗘𝗖𝗛 𝗡𝗘𝗪𝗦\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Stay updated with Simon Ban Checker.\n\n"
            "📌 Bot updates\n"
            "🆕 New features\n"
            "🔧 Maintenance notices\n"
            "📢 Important announcements\n\n"
            "👇 Subscribe to our channel",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "home":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔎 Check WhatsApp",
                    callback_data="check"
                ),
                InlineKeyboardButton(
                    "📦 Bulk Check",
                    callback_data="bulk"
                )
            ],
            [
                InlineKeyboardButton(
                    "📜 My History",
                    callback_data="history"
                ),
                InlineKeyboardButton(
                    "🌍 Language",
                    callback_data="language"
                )
            ],
            [
                InlineKeyboardButton(
                    "👤 Guest Mode",
                    callback_data="guest"
                ),
                InlineKeyboardButton(
                    "📖 How To Check",
                    callback_data="help"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 Channel News",
                    callback_data="news"
                )
            ]
        ]

        await query.edit_message_text(
            "🛡️ 𝗦𝗜𝗠𝗢𝗡 𝗕𝗔𝗡 𝗖𝗛𝗘𝗖𝗞𝗘𝗥\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "👋 Welcome back!\n\n"
            "Choose an option below:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "cancel":

        context.user_data.pop("waiting_for_number", None)
        context.user_data.pop("waiting_for_bulk", None)

        await query.edit_message_text(
            "❌ 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗡𝗖𝗘𝗟𝗟𝗘𝗗\n\n"
            "Use /start to return to the main menu."
        )
