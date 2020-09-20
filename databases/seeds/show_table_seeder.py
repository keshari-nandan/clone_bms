from orator.seeds import Seeder
from app.models.Movie import Movie
from app.models.Screen import Screen
import random

show_timings = [
    ['09:00 AM', '12:00 PM', '03:30 PM', '07:30 PM', '10:00 PM'],
    ['10:00 AM', '12:30 PM', '04:00 PM', '08:30 PM', '11:30 PM'],
    ['08:30 AM', '11:30 AM', '02:30 PM', '05:30 PM', '09:30 PM'],
]


class ShowTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """

        start_day = 20
        max_day = start_day + 5
        movies = Movie.all().pluck('id')
        screens = Screen.all().pluck('id')
        while start_day < max_day:
            for screen in screens:
                shows = random.choice(show_timings)
                for show in shows:
                    self.db.table('movie_shows').insert({
                        'movie_id': random.choice(movies),
                        'screen_id': screen,
                        'show_time': show,
                        'show_date': '2020-09-{0}'.format(start_day)
                    })
            start_day += 1
