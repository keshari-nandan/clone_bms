"""Base Database Seeder Module."""

from orator.seeds import Seeder
from .user_table_seeder import UserTableSeeder
from .city_table_seeder import CityTableSeeder
from .movie_table_seeder import MovieTableSeeder
from .theater_table_seeder import TheaterTableSeeder
from .show_table_seeder import ShowTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """Run the database seeds."""
        self.call(CityTableSeeder)
        self.call(MovieTableSeeder)
        self.call(TheaterTableSeeder)
        self.call(ShowTableSeeder)
