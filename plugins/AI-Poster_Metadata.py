# This bot is developed by **RETOUCH**
from hydrogram import Client, filters, types
from info import POWERED_BY, TECH_DESIGN, CIRC_DESIGN
from imdb import IMDb

ia = IMDb()

async def get_movie_card(movie_id):
    movie = ia.get_movie(movie_id)
    title = movie.get('title')
    year = movie.get('year')
    rating = movie.get('rating')
    poster = movie.get('full-size cover url')
    genres = ", ".join(movie.get('genres', []))
    
    caption = (
        f"{TECH_DESIGN}\n"
        f"🎬 **MOVIE:** `{title} ({year})`\n"
        f"{CIRC_DESIGN}\n"
        f"⭐ **RATING:** `{rating}/10`\n"
        f"🎭 **GENRE:** `{genres}`\n\n"
        f"**{POWERED_BY}**\n"
        f"{TECH_DESIGN}"
    )
    return poster, caption

# Logic: Call this inside your callback_query before showing the Ad-Gate.
