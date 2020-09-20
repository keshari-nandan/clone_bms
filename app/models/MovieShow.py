"""MovieShow Model."""
from config.database import Model


class MovieShow(Model):
    """MovieShow Model."""
    __table__ = 'movie_shows'

    __casts__ = {'show_time': 'string', 'show_date': 'string'}
