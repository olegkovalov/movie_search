def pretty_date(dt):
    return dt.strftime('%b %d, %Y %H:%M:%S') if dt else ''

filters_map = {
    'pretty_date': pretty_date,
}
