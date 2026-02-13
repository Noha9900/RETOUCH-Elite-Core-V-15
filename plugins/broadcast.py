# This bot is developed by **RETOUCH**
import asyncio
import time
from hydrogram import Client, filters
from hydrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from info import ADMINS, POWERED_BY
from database import db # Uses the database logic we built earlier

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_handler(bot, message):
    all_users = await db.users.find().to_list(length=None)
    broadcast_msg = message.reply_to_message
    
    total = len(all_users)
    success = 0
    blocked = 0
    failed = 0
    
    start_time = time.time()
    status_msg = await message.reply_text(f"**⚡ RETOUCH BROADCAST INITIALIZED**\nTargeting `{total}` users...")

    for user in all_users:
        try:
            await broadcast_msg.copy(chat_id=user['id'])
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await broadcast_msg.copy(chat_id=user['id'])
            success += 1
        except (UserIsBlocked, InputUserDeactivated):
            blocked += 1
        except Exception:
            failed += 1
        
        # Update progress every 20 users so it's ultra-fast
        if success % 20 == 0:
            try:
                await status_msg.edit(f"**RETOUCH BROADCAST IN PROGRESS**\n\n✅ Success: `{success}`\n🚫 Blocked: `{blocked}`\n❌ Failed: `{failed}`")
            except:
                pass

    time_taken = round(time.time() - start_time, 2)
    await status_msg.edit(
        f"**╔════════════════════════╗\n  BROADCAST COMPLETED ✅  \n╚════════════════════════╝**\n\n"
        f"👤 Total Users: `{total}`\n"
        f"🚀 Time Taken: `{time_taken}s`\n\n"
        f"{POWERED_BY}"
    )
