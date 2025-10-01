from typing import List

import pytest
from bm25_rs import BM25Okapi


@pytest.fixture
def sample_corpus():
    return [
        "Hello there good man!",
        "It is quite windy in London",
        "How is the weather today?",
        "This is a longer document with more words to test the implementation",
        "Short doc"
    ]


@pytest.fixture
def bm25(sample_corpus):
    # tokenized_corpus = [doc.lower().split() for doc in sample_corpus]
    return BM25Okapi(sample_corpus)


def test_initialization(bm25, sample_corpus):
    assert bm25.corpus_size == len(sample_corpus)


def test_get_scores(bm25):
    query = "weather today london".split()
    scores = bm25.get_scores(query)
    assert len(scores) == bm25.corpus_size
    assert all(isinstance(score, float) for score in scores)


def test_get_batch_scores(bm25):
    query = "weather today london".split()
    doc_ids = [0, 2, 4]
    scores = bm25.get_batch_scores(query, doc_ids)
    assert len(scores) == len(doc_ids)
    assert all(isinstance(score, float) for score in scores)


def test_get_top_n(bm25, sample_corpus):
    query = "weather today london".split()
    top_docs = bm25.get_top_n(query, sample_corpus, n=2)
    assert len(top_docs) == 2
    for doc in top_docs:
        assert doc[0] in sample_corpus


def test_custom_tokenizer(sample_corpus):
    def custom_tokenizer(text: str) -> List[str]:
        return text.lower().split()

    bm25_custom = BM25Okapi(sample_corpus, tokenizer=custom_tokenizer)
    assert bm25_custom.corpus_size == len(sample_corpus)
