import urllib, urllib.request

import Document


class Arxiv:
    def __init__(self):
        self.query_url = 'http://export.arxiv.org/api/query?search_query='

    def query(self, keywords, max_results):
        if len(keywords) < 1: return []
        url = self.query_url + 'all:' + keywords[0]

        if len(keywords) > 1:
            for keyword in keywords[1:]:
                url += '+AND+'
                url += 'all:' + keyword

        url += '&max_results=' + str(max_results)

        results = urllib.request.urlopen(url)
        print(results.read().decode('utf-8'))

if __name__ == '__main__':
    arxiv = Arxiv()
    arxiv.query(['covid', 'vaccine'], 10)
