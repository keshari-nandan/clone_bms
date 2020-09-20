from masonite.api.resources import Resource
from masonite.api.serializers import JSONSerializer
from app.models.Movie import Movie
from app.models.City import City
from app.models.Theater import Theater
from masonite.request import Request


class CityWiseMovieResource(Resource, JSONSerializer):
    model = Movie
    methods = ['city_wise_movies']

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

    def routes(self):
        """
        Override the default route method to user own method
        """
        routes = []
        if 'city_wise_movies' in self.methods:
            routes.append(self.__class__(self.route_url,
                                         ['GET']).middleware(*self.list_middleware))

        return routes

    def get_response(self):
        """Gets the response that should be returned from this resource
         - Override the default get_response from resource to get the params and prepare the response
        """

        # Set the Guard class.
        from masonite.auth import Auth
        auth = self.request.app().make(Auth)
        auth.set(self.guard)

        response = None
        # If the authenticate method did not return a response, continue on to one of the CRUD responses
        if not response:
            response = self.request.app().resolve(getattr(self, 'city_wise_movies'))
        # If the resource needs it's own serializer method
        if hasattr(self, 'serialize'):
            response = self.serialize(response)
        # If the resource needs it's own serializer method
        if hasattr(self, 'filter'):
            response = self.filter(response)

        if response is None:
            self.request.status(404)
            return {"message": "Resource Not Found"}

        return response
