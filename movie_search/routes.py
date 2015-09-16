def add_routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('search', '/')
    config.add_route('movie_list', '/history')
