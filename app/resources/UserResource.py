from masonite.api.resources import Resource
from masonite.api.serializers import JSONSerializer
from app.models.User import User
from masonite.auth import Auth
from masonite.request import Request
from masonite.helpers import password


class UserResource(Resource, JSONSerializer):
    model = User
    methods = ['register']
    __custom_method_name__ = 'register'
    without = ['password']

    def register(self, request: Request):
        """Logic to create data from a given model
        """
        try:
            record = User.create({
                'name': request.input('name'),
                'email': request.input('email'),
                'password': password(request.input('password')),
            })
        except Exception as e:
            return {'error': str(e)}
        return record

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
