import requests

from bson import json_util
from pyramid.view import view_defaults, view_config

from movie_search.models.movie import Movie
from movie_search.settings import OMDB_URL


class BaseView(object):
    def __init__(self, request):
        self.req = request


@view_defaults(route_name='search', renderer='search.html')
class SearchView(BaseView):

    @view_config(request_method='GET')
    def get(self):
        q = self.req.params.get('q')
        movie = None
        title = None

        if q and len(q) > 3:
            title, poster_url = self.get_movie_info(q)

        if title:
            movie = self.get_or_create_movie(title, poster_url)

        return {
            'movie': movie,
            'q': q,
        }

    def get_movie_info(self, q):
        title, poster_url = None, None
        params = dict(t=q, plot='short', r='json')
        r = requests.get(OMDB_URL, params=params)
        content = json_util.loads(r.content)
        if not content.get('Error'):
            title = content.get('Title')
            if content.get('Poster') != 'N/A':
                poster_url = content.get('Poster')
        return title, poster_url

    def get_or_create_movie(self, title, poster_url):
        if not Movie.objects(title=title).count():
            movie = Movie(title=title).save()
        else:
            movie = Movie.objects(title=title).first()

        if poster_url:
            movie.update_poster(poster_url)
            movie.save()
        return movie


@view_defaults(route_name='movie_list', renderer='movies.html')
class MovieListView(BaseView):

    @view_config(request_method='GET')
    def get(self):
        return {
            'movie_list': Movie.objects().order_by('date')
        }
