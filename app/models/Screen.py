"""Screen Model."""
from orator.orm import has_many

from config.database import Model
from .MovieShow import MovieShow


class Screen(Model):
    """Screen Model."""

    __table__ = 'screens'

    @has_many('screen_id', 'id')
    def shows(self):
        return MovieShow
