# This bot is developed by **RETOUCH**
from hydrogram import Client, filters, types
from info import TECH_BANNER, POWERED_BY, TECH_DESIGN

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(bot, message):
    # Professional Technical Welcome
    text = (
        f"{TECH_BANNER}\n"
        f"**WELCOME TO RETOUCH CORE v15.0**\n"
        f"{TECH_DESIGN}\n"
        "I am an AI-powered media filter engine.\n"
        "Just send me a movie name to begin.\n\n"
        "⚡ **Speed:** `Ultra-Fast`\n"
        "🧠 **Search:** `AI-Intelligent`\n"
        "🛡️ **Security:** `High-Level`\n\n"
        f"**{POWERED_BY}**"
    )
    
    buttons = [
        [types.InlineKeyboardButton("📢 Updates Channel", url="https://t.me/your_channel")],
        [types.InlineKeyboardButton("🛠 Support Group", url="https://t.me/your_support")]
    ]
    
    await message.reply_text(text, reply_markup=types.InlineKeyboardMarkup(buttons))
