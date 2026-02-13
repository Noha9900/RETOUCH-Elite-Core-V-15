# This bot is developed by **RETOUCH**
from hydrogram import Client, filters, types
from hydrogram.errors import UserNotParticipant
from info import FSUB_CHANNEL, POWERED_BY

async def check_fsub(bot, message):
    if not FSUB_CHANNEL:
        return True
    try:
        user = await bot.get_chat_member(FSUB_CHANNEL, message.from_user.id)
        if user.status == "kicked":
            await message.reply_text("❌ You are banned from using this bot.")
            return False
        return True
    except UserNotParticipant:
        buttons = [
            [types.InlineKeyboardButton("Join Updates Channel 📣", url=f"https://t.me/your_channel")],
            [types.InlineKeyboardButton("Try Again 🔄", callback_data="check_fsub")]
        ]
        await message.reply_text(
            f"**⚠️ ACCESS DENIED**\n\nYou must join our updates channel to use the RETOUCH Engine.\n\n{POWERED_BY}",
            reply_markup=types.InlineKeyboardMarkup(buttons)
        )
        return False
