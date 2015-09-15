from pyramid.view import view_config


@view_config(route_name='search', renderer='json')
def search(request):
    return {}
