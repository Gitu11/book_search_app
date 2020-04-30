"""
Add Unit tests for the query module.
"""
from book_search_app.core.query import relevance_ranking


def test_relevance_ranking():
    word_map = {0: [[1], [11, 16], [22]], 7: [[9]], 48: [[12, 24]]}
    rank_list = relevance_ranking(word_map)
    assert len(word_map) == len(rank_list)
    assert rank_list == [0, 48, 7]
