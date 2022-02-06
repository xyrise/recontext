import json
import requests

from Document import Document


class SemanticScholar:
    def __init__(self):
        self.query_url = 'https://api.semanticscholar.org/graph/v1/paper/search?'

    def queryURL(self, keywords, start_results, max_results, fields):
        if len(keywords) < 1: return None
        if len(fields) < 1: return None
        url = self.query_url + 'query=' + keywords[0]

        if len(keywords) > 1:
            for keyword in keywords[1:]:
                url += '+' + keyword

        url += '&offset=' + str(start_results)
        url += '&limit=' + str(max_results)
        url += '&fields=' + fields[0]

        if len(fields) > 1:
            for field in fields[1:]:
                url += ',' + field

        return url

    def queryAll(self, keywords, max_results, start=0):
        if len(keywords) < 1: return none
        url = self.queryURL(keywords, start, max_results, [
            'url',
            'title',
            'abstract',
            'year',
            'authors',
            'citationCount'
            ])

        raw_results = requests.get(url).json()['data']
        results = []

        for raw_result in raw_results:
            result = Document(
                    url=raw_result['url'],
                    title=raw_result['title'],
                    authors=[author['name'] for author in raw_result['authors']],
                    published=raw_result['year'],
                    abstract=raw_result['abstract'],
                    citationCount=raw_result['citationCount']
                    )
            results.append(result)

        return results

    def queryDates(self, keywords, max_results, start=0):
        if len(keywords) < 1: return none
        url = self.queryURL(keywords, start, max_results, ['year'])

        raw_results = requests.get(url).json()['data']
        results = []

        for raw_result in raw_results:
            result = Document(published=raw_result['year'])
            results.append(result)

        return results



if __name__ == '__main__':
    semantic_scholar = SemanticScholar()
    print(semantic_scholar.queryAll(['covid', 'vaccine'], max_results=10))
    print(semantic_scholar.queryDates(['covid', 'vaccine'], start=11, max_results=15))

