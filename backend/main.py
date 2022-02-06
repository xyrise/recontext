from fastapi import FastAPI, Query

from typing import List
from Arxiv import Arxiv
from popularitytrend import get_trend
from textsimilarity import text_similarity


app = FastAPI()


@app.get('/')
async def root():
    arxiv = Arxiv()
    docs = text_similarity(arxiv.queryAll(['covid', 'pandemic'], 10))
    return docs

@app.get('/research/')
async def research(max: int, key: List[str] = Query(..., min_length=1)):
    arxiv = Arxiv()
    docs = text_similarity(arxiv.queryAll(key, max))
    return docs

@app.get('/trend/')
async def trend(max: int, key: List[str] = Query(..., min_length=1)):
    arxiv = Arxiv()
    return get_trend(arxiv.queryDates(key, max*10))