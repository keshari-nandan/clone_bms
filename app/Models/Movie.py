"""Movie Model."""

from config.database import Model


class Movie(Model):
    """Movie Model."""
    __table__ = 'movies'
    pass