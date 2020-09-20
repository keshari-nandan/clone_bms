from app.resources.BaseResourse import BaseResource
from app.models.MovieShow import MovieShow
from app.models.MovieBooking import MovieBooking
from app.models.Screen import Screen
from masonite.request import Request


class ShowSeatAvailabilityResource(BaseResource):
    model = MovieShow
    methods = ['show_seat_check']
    __custom_method_name__ = 'show_seat_check'

    def show_seat_check(self, request: Request):
        show_id = request.param('id')
        show = MovieShow.find(show_id)
        if not show:
            raise ValueError('Request contains invalid data.')
        bookings_for_show = MovieBooking.where('show_id', show.id).get().pluck('id')
        screen = Screen.where('id', show.screen_id).first_or_fail()
        response = {
            "id": show.id,
            "movie_id": show.movie_id,
            "screen_id": show.screen_id,
            "show_time": show.show_time,
            "show_date": show.show_date,
            "total_seats": screen.seats,
            "available_seats": screen.seats - len(bookings_for_show)
        }
        return response


