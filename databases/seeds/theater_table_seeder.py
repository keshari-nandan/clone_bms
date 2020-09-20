from orator.seeds import Seeder
from config.factories import factory
from app.models.Theater import Theater
from app.models.City import City
from app.models.Screen import Screen
import random

ran_range = [1, 2, 3]
rand_seats = [60, 57, 120, 200, 83]


@factory.define(Theater)
def theaters_factory(faker):
    cities = City.all().pluck('id')
    return {
        'name': faker.name(),
        'city_id': random.choice(cities),
    }


@factory.define(Screen)
def screens_factory(faker):
    return {
        'name': faker.name(),
        'seats': random.choice(rand_seats),
    }


class TheaterTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        theaters = factory(Theater, 10).create()
        for theater in theaters:
            screen_count = random.choice(ran_range)
            while screen_count > 0:
                theater.screens().save(factory(Screen).make())
                screen_count -= 1
