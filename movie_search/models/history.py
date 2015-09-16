from datetime import datetime

from mongoengine import Document, ReferenceField, DateTimeField

from movie import Movie


class History(Document):
    movie = ReferenceField(Movie)
    created = DateTimeField(default=datetime.now())
