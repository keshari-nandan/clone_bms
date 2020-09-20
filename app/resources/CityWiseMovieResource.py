from app.resources.BaseResourse import BaseResource
from app.models.Movie import Movie
from app.models.City import City
from app.models.Theater import Theater
from masonite.request import Request


class CityWiseMovieResource(BaseResource):
    model = Movie
    methods = ['city_wise_movies']
    __custom_method_name__ = 'city_wise_movies'

    def city_wise_movies(self, request: Request):
        city_name = request.param('city').capitalize()
        city = City.where('name', city_name).first_or_fail()
        theaters = Theater.with_('screens.shows').where('city_id', city.id).get()
        movies = []
        for theater in theaters:
            for screen in theater.screens:
                for show in screen.shows:
                    if show.movie_id not in movies:
                        movies.append(show.movie_id)

        return self.model.with_('casts', 'crews', 'genres', 'languages').where_in('id', movies).get()
