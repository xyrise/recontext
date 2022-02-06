from typing import List

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from Arxiv import Arxiv
from popularitytrend import get_trend
from textsimilarity import text_similarity


app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
)


@app.get('/')
async def root():
    arxiv = Arxiv()
    docs = text_similarity(arxiv.queryAll(['covid', 'pandemic'], 10))
    return docs

@app.get('/research/')
async def research(max: int, key: List[str] = Query(..., min_length=1)):
    semantic_scholar = SemanticScholar()
    docs = text_similarity(semantic_scholar.queryAll(key, max))
    return docs

@app.get('/trend/')
async def trend(max: int, key: List[str] = Query(..., min_length=1)):
    semantic_scholar = SemanticScholar()
    return get_trend(semantic_scholar.queryDates(key, max*10))
