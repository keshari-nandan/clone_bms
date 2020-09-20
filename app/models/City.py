"""City Model."""
from orator.orm import has_many

from config.database import Model
from .Theater import Theater


class City(Model):
    """City Model."""

    __table__ = 'cities'

    @has_many('city_id', 'id')
    def theaters(self):
        return Theater
