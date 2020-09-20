"""Web Routes."""

from masonite.routes import Get, Post
from app.resources.CityWiseMovieResource import CityWiseMovieResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    # Movie Routes
    CityWiseMovieResource('/api/city/@city/movies').routes()
]
