from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Document:
    def __init__(self, url, title, abstract):
        self.url = url
        self.title = title
        self.abstract = abstract
        self.keywords = []

def text_similarity(documents):
    vect = TfidfVectorizer(stop_words="english") 
    tfidf = vect.fit_transform([doc.abstract for doc in documents])
    pairwise_similarity = tfidf * tfidf.T
    data = tfidf.todense().tolist()
    names = vect.get_feature_names_out()
    df = pd.DataFrame(data, columns=names)
    for i in df.iterrows():
        documents[i[0]].keywords = (i[1].sort_values(ascending=False)[:2].index.tolist())
    similarities = pairwise_similarity.toarray().sum(axis=1)
    sim_indexes = [(similarities[i], i) for i in range(len(similarities))]
    sorted_sims = sorted(sim_indexes)
    return [documents[i[1]] for i in sorted_sims]