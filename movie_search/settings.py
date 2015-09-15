import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
POSTER_ROOT = os.path.join(STATIC_ROOT, 'poster')

OMDB_URL = 'http://www.omdbapi.com'
