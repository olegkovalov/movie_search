def pretty_date(dt):
    return dt.strftime('%b %d, %Y') if dt else ''

filters_map = {
    'pretty_date': pretty_date,
}
