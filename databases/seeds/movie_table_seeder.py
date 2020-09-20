from orator.seeds import Seeder
from config.factories import factory

from app.models.Cast import Cast
from app.models.Crew import Crew
from app.models.Movie import Movie
from app.models.Language import Language
from app.models.Genre import Genre
import random

play_times = [145, 176, 152, 149, 145, 161, 132, 155]
languages = ['English', 'Hindi', 'Spanish']
genres = ['Action', 'Horror', 'Drama', 'Comedy', 'Romance', 'Science Fiction', 'Thriller', 'Adventure']
ran_range = [1, 2, 3]


@factory.define(Movie)
def movies_factory(faker):
    return {
        'name': faker.name(),
        'description': faker.text(),
        'play_time': random.choice(play_times),
        'release_date': faker.date(),
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


@factory.define(Language)
def languages_factory(faker):
    return {
        'name': random.choice(languages),
    }


@factory.define(Genre)
def genres_factory(faker):
    return {
        'name': random.choice(genres),
    }


class MovieTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        movies = factory(Movie, 10).create()
        for movie in movies:
            no_of_casts = random.choice(ran_range)
            while no_of_casts > 0:
                movie.casts().save(factory(Cast).make())
                no_of_casts -= 1

            no_of_crews = random.choice(ran_range)
            while no_of_crews > 0:
                movie.crews().save(factory(Crew).make())
                no_of_crews -= 1

            no_of_genres = random.choice(ran_range)
            while no_of_genres > 0:
                movie.genres().save(factory(Genre).make())
                no_of_genres -= 1

            no_of_languages = random.choice([1, 2])
            while no_of_languages > 0:
                movie.languages().save(factory(Language).make())
                no_of_languages -= 1
