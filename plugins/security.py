# This bot is developed by **RETOUCH**
from hydrogram import Client, filters
from hydrogram.types import ChatPermissions
from info import ADMINS, POWERED_BY

# Protect groups from links and spam
@Client.on_message(filters.group & ~filters.user(ADMINS))
async def security_guard(bot, message):
    # 1. Protect from Links (Http/Https/T.me)
    if message.entities:
        for entity in message.entities:
            if entity.type in ["url", "text_link"]:
                await message.delete()
                warning = await message.reply_text(
                    f"**⚠️ UNAUTHORIZED LINK DETECTED**\n"
                    f"User: {message.from_user.mention}\n"
                    f"**Action:** Message Deleted by RETOUCH Security.\n\n"
                    f"{POWERED_BY}"
                )
                # Delete warning after 10 seconds to keep group clean
                await asyncio.sleep(10)
                await warning.delete()
                return

    # 2. Basic Anti-Spam (Detects repetitive characters or flood)
    if len(message.text or "") > 1000:
        await message.delete()
        await bot.restrict_chat_member(
            message.chat.id, 
            message.from_user.id,
            ChatPermissions(can_send_messages=False)
        )
        await message.reply_text(f"**🚫 SPAM DETECTED**\n{message.from_user.mention} has been muted.")
