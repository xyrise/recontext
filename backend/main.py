from fastapi import FastAPI, Query

from typing import List
from Arxiv import Arxiv
from Document import Document
from textsimilarity import text_similarity


app = FastAPI()


@app.get('/')
async def root():
    arxiv = Arxiv()
    docs = text_similarity(arxiv.query(['covid', 'pandemic'], 10))
    return docs

@app.get('/research/')
async def research(max: int, key: List[str] = Query(..., min_length=1)):
    arxiv = Arxiv()
    docs = text_similarity(arxiv.query(key, max))
    return docs
