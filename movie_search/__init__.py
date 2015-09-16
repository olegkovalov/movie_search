import pymongo

from urlparse import urlparse
from mongoengine import connect
from pyramid.config import Configurator

from movie_search import settings
from movie_search.filters import filters_map
from movie_search.routes import add_routes


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    settings.setdefault('jinja2.filters', {}).update(filters_map)

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_jinja2_search_path('movie_search:templates', name='.html')

    add_routes(config)

    db_url = urlparse(settings['mongo_uri'])
    db_settings = {'host': db_url.hostname, 'port': db_url.port}
    config.registry.db = pymongo.Connection(**db_settings)
    config.registry.db_url = db_url
    connect(db_url.path[1:], **db_settings)

    config.scan()
    return config.make_wsgi_app()
