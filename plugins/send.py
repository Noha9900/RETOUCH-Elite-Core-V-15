# This bot is developed by **RETOUCH**
from hydrogram import Client, filters
from info import ADMINS, POWERED_BY, TECH_DESIGN, CIRC_DESIGN
from utils.logger import logger

@Client.on_message(filters.command("send") & filters.user(ADMINS))
async def send_to_user(bot, message):
    if len(message.command) < 3:
        return await message.reply_text("**Usage:** `/send {user_id} {text}`")

    target_id = message.command[1]
    text_to_send = message.text.split(None, 2)[2]

    try:
        branded_msg = (
            f"{TECH_DESIGN}\n"
            f"📩 **MESSAGE FROM SYSTEM ADMIN**\n"
            f"{CIRC_DESIGN}\n\n"
            f"{text_to_send}\n\n"
            f"**{POWERED_BY}**\n"
            f"{TECH_DESIGN}"
        )
        await bot.send_message(int(target_id), branded_msg)
        await message.reply_text(f"✅ **Message successfully delivered to `{target_id}`**")
    except Exception as e:
        await message.reply_text(f"❌ **Failed to send:** `{str(e)}`")
        logger.error(f"Send Error: {e}")

@Client.on_message(filters.command("send_file") & filters.user(ADMINS))
async def send_file_to_user(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("❌ **Reply to a file/video to use this command.**\n**Usage:** `/send_file {user_id}`")

    if len(message.command) < 2:
        return await message.reply_text("❌ **Usage:** `/send_file {user_id}` (while replying to a file)")

    target_id = message.command[1]
    file_to_send = message.reply_to_message

    try:
        # Copy the replied file to the target user
        await file_to_send.copy(chat_id=int(target_id))
        await message.reply_text(f"✅ **Media successfully sent to `{target_id}`**")
    except Exception as e:
        await message.reply_text(f"❌ **Failed to send file:** `{str(e)}`")
