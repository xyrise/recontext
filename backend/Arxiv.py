import feedparser
import urllib, urllib.request

from Document import Document


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

        raw_results = feedparser.parse(url)['entries']
        results = []

        for raw_result in raw_results:
            result = Document(
                    url=raw_result['link'],
                    title=raw_result['title'],
                    authors=[author.name for author in raw_result['authors']],
                    published=raw_result['published'],
                    abstract=raw_result['summary']
                    )
            results.append(result)

        return results


if __name__ == '__main__':
    arxiv = Arxiv()
    arxiv.query(['covid', 'vaccine'], 10)
