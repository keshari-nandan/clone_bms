import jwt
from masonite.api.resources import Resource
from masonite.api.serializers import JSONSerializer
from masonite.api.authentication import JWTAuthentication
from app.models.User import User
from masonite.auth import Auth
from masonite.request import Request
from app.models.MovieShow import MovieShow
from app.models.MovieBooking import MovieBooking


class UserBookingResource(Resource, JSONSerializer, JWTAuthentication):
    model = User
    methods = ['book_show']
    __custom_method_name__ = 'book_show'

    def book_show(self, request: Request):
        """Logic to create data from a given model
        """
        show_id = request.param('show')
        show = MovieShow.find(show_id)
        if not show:
            raise ValueError('Invalid request')

        seats = request.input('seats')
        user = request.user()
        if seats < 1:
            raise ValueError('You must select at least one seat for this booking')

        while seats > 0:
            MovieBooking.create({
                "user_id": user.id,
                "show_id": show.id
            })
        return {"message": "Seat has been confirmed. You will receive an email shortly with details."}

    def routes(self):
        """
        Override the default route method to user own method
        """
        routes = []
        if self.__custom_method_name__ in self.methods:
            routes.append(self.__class__(self.route_url, ['POST']).middleware(*self.list_middleware))
        return routes

    def get_response(self):
        """Gets the response that should be returned from this resource
         - Override the default get_response from resource to get the params and prepare the response
        """

        # Set the Guard class.
        auth = self.request.app().make(Auth)
        auth.set(self.guard)

        response = None
        # If the authenticate method did not return a response, continue on to one of the CRUD responses
        if not response:
            response = self.request.app().resolve(getattr(self, self.__custom_method_name__))
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
