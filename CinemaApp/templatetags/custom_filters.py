from django import template
from datetime import datetime

register = template.Library()

@register.filter
def filter_movies_by_date(movies, date):
    """Filter movies to show only those scheduled to start on or after the given date."""
    filtered_movies = set()
    for movie in movies:
        if movie.schedule_set.filter(start_time__date=date).exists():
            filtered_movies.add(movie)
    return filtered_movies

