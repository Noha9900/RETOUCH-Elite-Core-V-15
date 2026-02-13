# This bot is developed by **RETOUCH**
from hydrogram import Client, filters, types
from info import LOG_CHANNEL, POWERED_BY

@Client.on_callback_query(filters.regex(r"^request_"))
async def handle_request(bot, query):
    user = query.from_user
    movie_name = query.data.split("_", 1)[1]

    # 1. Send Request to Admin Log Channel
    if LOG_CHANNEL:
        request_text = (
            f"**📥 NEW MOVIE REQUEST**\n"
            f"**○───────────────────○**\n"
            f"👤 **User:** {user.first_name} (ID: `{user.id}`)\n"
            f"🎬 **Movie:** `{movie_name.upper()}`\n"
            f"**○───────────────────○**\n"
            f"{POWERED_BY}"
        )
        await bot.send_message(LOG_CHANNEL, request_text)

    # 2. Confirm to User
    await query.answer("✅ Request Sent! We will upload it soon.", show_alert=True)
    await query.message.edit_text(
        f"**📥 REQUEST REGISTERED**\n\nYour request for `{movie_name}` has been sent to the **RETOUCH TEAM**. We will notify you once it's available.\n\n{POWERED_BY}"
    )

# Logic to be added inside your auto_filter.py (when no results are found):
# if not versions:
#     btn = [[types.InlineKeyboardButton("📤 Request This Movie", callback_data=f"request_{message.text}")]]
#     return await message.reply_text(f"**[!] '{message.text}' is not in our database.**", reply_markup=types.InlineKeyboardMarkup(btn))
