from orator.seeds import Seeder
from config.factories import factory

from app.models.Cast import Cast
from app.models.Crew import Crew
from app.models.Movie import Movie


@factory.define(Movie)
def movies_factory(faker):
    return {
        'name': faker.name(),
        'description': faker.text()
    }


@factory.define(Cast)
def casts_factory(faker):
    return {
        'name': faker.name(),
        'role': 'Director',
        'role_name': faker.name(),
    }


@factory.define(Crew)
def crews_factory(faker):
    return {
        'name': faker.name(),
        'role': 'Writer'
    }


class MovieTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        movies = factory(Movie, 10).create()
        for movie in movies:
            movie.casts().save(factory(Cast).make())
            movie.crews().save(factory(Crew).make())

