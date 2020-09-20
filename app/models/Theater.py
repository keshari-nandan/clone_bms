"""Theater Model."""
from orator.orm import has_many
from .Screen import Screen
from config.database import Model


class Theater(Model):
    """Theater Model."""

    __table__ = 'theaters'

    @has_many('theater_id', 'id')
    def screens(self):
        return Screen

