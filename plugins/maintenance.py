# This bot is developed by **RETOUCH**
from hydrogram import Client, filters, types
from info import ADMINS, POWERED_BY, TECH_BANNER, CIRC_DESIGN

# Local memory to track status without hitting DB every time
IS_MAINTENANCE = False

@Client.on_message(filters.command("maintenance") & filters.user(ADMINS))
async def toggle_maintenance(bot, message):
    global IS_MAINTENANCE
    IS_MAINTENANCE = not IS_MAINTENANCE
    status = "ENABLED 🟢" if IS_MAINTENANCE else "DISABLED 🔴"
    await message.reply_text(f"**[!] MAINTENANCE MODE {status}**\n\n{POWERED_BY}")

# Middleware-style check to block users
@Client.on_message(filters.private & ~filters.user(ADMINS), group=-1)
async def maintenance_check(bot, message):
    if IS_MAINTENANCE:
        text = (
            f"{TECH_BANNER}\n"
            f"**⚠️ SYSTEM UNDER MAINTENANCE**\n"
            f"{CIRC_DESIGN}\n"
            "Our engineers are currently upgrading the \n"
            "**RETOUCH CORE v15.0** database.\n\n"
            "Please try again in a few minutes.\n"
            f"**{POWERED_BY}**"
        )
        await message.reply_text(text)
        message.stop_propagation() # Prevents other plugins from running
