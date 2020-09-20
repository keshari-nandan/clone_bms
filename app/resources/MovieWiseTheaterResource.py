from app.resources.BaseResourse import BaseResource
from app.models.Theater import Theater
from masonite.request import Request


class MovieWiseTheaterResource(BaseResource):
    model = Theater
    methods = ['movie_wise_theaters']
    __custom_method_name__ = 'movie_wise_theaters'

    def movie_wise_theaters(self, request: Request):
        movie_id = request.param('movie')
        # This orm with method does not support filtering that's why it's pulling all the record.
        # Other ways of filtering will be join, but since in other api's I have used orm, so to maintain the sanity
        # I am not using join here, but it totally possible
        theaters = Theater.with_('screens.shows').where_has('screens', lambda screen: screen.where_has('shows', lambda show: show.where('movie_id', movie_id))).get()
        return theaters


