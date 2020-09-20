from orator.seeds import Seeder
from config.factories import factory
from app.models.Theater import Theater
from app.models.City import City
from app.models.Screen import Screen
import random

cities = City.all().pluck('id')
ran_range = [1, 2, 3]


@factory.define(Theater)
def theaters_factory(faker):
    return {
        'name': faker.name(),
        'city_id': random.choice(cities),
    }

@factory.define(Theater)
def screens_factory(faker):
    return {
        'name': faker.name(),
        'city_id': random.choice(cities),
    }


class TheaterTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        theaters = factory(Theater, 10).create()
        for theater in theaters:
            screens = random.choice(ran_range)
            while screens > 0:
                theater.screens().save(factory(Screen).make())
                screens -= 1
