# This bot is developed by **RETOUCH**
from hydrogram import Client, filters, types
from info import POWERED_BY, TECH_BANNER
from imdb import IMDb

ia = IMDb()

@Client.on_message(filters.command("trending") & filters.private)
async def get_trending(bot, message):
    top_movies = ia.get_top250_movies()[:10] # Fetches Top 10 from IMDb
    
    text = f"{TECH_BANNER}\n**🔥 GLOBAL TRENDING MOVIES**\n\n"
    buttons = []
    
    for movie in top_movies:
        title = movie['title']
        year = movie.get('year', 'N/A')
        text += f"• {title} ({year})\n"
        # Clicking this triggers the auto-search logic we built
        buttons.append([types.InlineKeyboardButton(f"🔍 Search {title}", switch_inline_query_current_chat=title)])

    text += f"\n{POWERED_BY}"
    await message.reply_text(text, reply_markup=types.InlineKeyboardMarkup(buttons))
