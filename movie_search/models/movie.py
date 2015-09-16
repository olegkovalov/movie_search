from datetime import datetime

import requests
from mongoengine import Document, StringField, SequenceField, DateTimeField

from movie_search.utils.files import FileManage


class Movie(Document):
    _id = SequenceField(primary_key=True)
    title = StringField(required=True)
    poster = StringField()
    created = DateTimeField(default=datetime.now())

    def update_poster(self, poster_url):
        r = requests.get(poster_url)
        filename = self.title.lower() + '.' + r.headers['content-type'].split('/')[1]
        if not self.poster:
            f = FileManage(filename)
            self.poster = f.upload(r.content)
        else:
            f = FileManage(self.poster)
            if int(r.headers['content-length']) != f.get_length():
                f.remove()
                self.poster = f.upload(r.content)
