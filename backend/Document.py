import json

class Document:
    def __init__(self,
            url='',
            title='',
            authors=[],
            published='',
            abstract=''
    ):
        self.url = url
        self.title = title
        self.authors = authors
        self.published = published
        self.abstract = abstract
        self.keywords = []

    def __repr__(self):
        return json.dumps(self.__dict__)
