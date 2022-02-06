import feedparser

from Document import Document


class Arxiv:
    def __init__(self):
        self.query_url = 'http://export.arxiv.org/api/query?search_query='

    def queryURL(self, keywords, start_results, max_results):
        if len(keywords) < 1: return None
        url = self.query_url + 'all:"' + keywords[0] + '"'

        if len(keywords) > 1:
            for keyword in keywords[1:]:
                url += '+AND+'
                url += 'all:"' + keyword + '"'

        url += '&start=' + str(start_results)
        url += '&max_results=' + str(max_results)

        return url


    def queryAll(self, keywords, max_results, start=0):
        if len(keywords) < 1: return []
        url = self.queryURL(keywords, start, max_results)

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

    def queryDates(self, keywords, max_results, start=0):
        if len(keywords) < 1: return []
        url = self.queryURL(keywords, start, max_results)

        raw_results = feedparser.parse(url)['entries']
        results = []

        for raw_result in raw_results:
            result = Document(published=raw_result['published'])
            results.append(result)

        return results


if __name__ == '__main__':
    arxiv = Arxiv()
    print(arxiv.queryAll(['covid', 'vaccine'], max_results=10))
    print(arxiv.queryDates(['covid', 'vaccine'], start=11, max_results=15))
