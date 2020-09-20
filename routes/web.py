"""Web Routes."""

from masonite.routes import Get, Post
from app.resources.CityWiseMovieResource import CityWiseMovieResource
from app.resources.MovieWiseTheaterResource import MovieWiseTheaterResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    # Movie Routes
    CityWiseMovieResource('/api/city/@city/movies').routes(),
    MovieWiseTheaterResource('/api/movie/@movie/theaters').routes(),
]
