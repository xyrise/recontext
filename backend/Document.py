class Document:
    def __init__(self, url='', title='', author='', abstract_text=''):
        self.url = url
        self.title = title
        self.author = author
        self.abstract_text = abstract_text
        self.top_keywords = []
