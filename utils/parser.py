# This bot is developed by **RETOUCH**
import re
from spellchecker import SpellChecker
from imdb import IMDb

ia = IMDb()
spell = SpellChecker()

async def get_intelligent_results(query):
    # Spelling Logic
    words = query.split()
    misspelled = spell.unknown(words)
    if misspelled:
        query = " ".join([spell.correction(w) or w for w in words])

    # IMDb Search for Versions/Years
    results = ia.search_movie(query)
    movie_list = []
    for m in results[:5]:
        movie_list.append({
            "title": m['title'],
            "year": m.get('year', 'N/A'),
            "id": m.movieID
        })
    return movie_list, query
