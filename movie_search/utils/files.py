import os

from movie_search.settings import POSTER_ROOT


class FileManage(object):
    def __init__(self, filename):
        self.filename = filename

    def upload(self, input_file):
        filename = os.path.basename(self.filename)
        filename = filename.replace(' ', '_')
        file_path = os.path.join(POSTER_ROOT, filename)
        if os.path.exists(file_path):
            filename = self.get_unique_filename(filename)
            file_path = os.path.join(POSTER_ROOT, filename)
        with open(file_path, 'wb') as output_file:
            for chunk in input_file:
                output_file.write(chunk)
        return filename

    def remove(self):
        file_path = os.path.join(POSTER_ROOT, self.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def get_unique_filename(self, filename):
        new_name = ''
        counter = 0
        while True:
            new_name = filename.split('.')[0] + str(counter) + '.' + filename.split('.')[-1]
            file_path = os.path.join(POSTER_ROOT, new_name)
            counter += 1
            if not os.path.exists(file_path):
                break
        return new_name

    def get_length(self):
        file_path = os.path.join(POSTER_ROOT, self.filename)
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        return
