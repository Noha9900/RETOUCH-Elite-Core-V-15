# This bot is developed by **RETOUCH**
import asyncio, time
from hydrogram import Client, filters, types
from info import *
from database import db
from utils.parser import get_intelligent_results

bot = Client("RetouchBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(f"{TECH_BANNER}\nWelcome to the Retouch Network.\n\n{POWERED_BY}")

@bot.on_message(filters.text & filters.private & ~filters.command(["start", "bsetting"]))
async def auto_search(client, message):
    versions, corrected_name = await get_intelligent_results(message.text)
    if not versions:
        return await message.reply_text(f"**[!] No results found for '{message.text}'**")

    buttons = [[types.InlineKeyboardButton(f"🎬 {v['title']} ({v['year']})", callback_data=f"gate_{v['id']}")] for v in versions]
    await message.reply_text(
        f"{TECH_BANNER}\n**RESULTS FOR: {corrected_name.upper()}**\n\n{POWERED_BY}",
        reply_markup=types.InlineKeyboardMarkup(buttons)
    )

@bot.on_callback_query(filters.regex(r"^gate_"))
async def handle_gate(client, query):
    user_id = query.from_user.id
    if await db.has_access(user_id):
        # In a real bot, you'd fetch the specific file_id linked to the IMDb ID
        return await query.answer("Access Granted. Delivering files...", show_alert=True)

    # 30s Ad Timer
    for i in range(30, 0, -5):
        await query.edit_message_text(
            f"**╔════════════════════════╗\n  RETOUCH AD-SYSTEM LOADING  \n╚════════════════════════╝**\n\n"
            f"**Remaining:** `{i} Seconds`\n**Progress:** `{'█' * ((30-i)//3)}{'░' * (i//3)}`\n\n{POWERED_BY}"
        )
        await asyncio.sleep(5)
    
    await db.grant_access(user_id)
    await query.edit_message_text("**✅ ACCESS GRANTED!** 24h Pass Active. Search again to get your file.")

bot.run()
