"""
Module to write unit tests for the helper functions.
"""


from book_search_app.utils.helper import filter_stopwords, find_indexes


def test_filter_stopwords():
    test_data = ['this', 'is', 'a', 'unittest']
    out = filter_stopwords(test_data)
    assert out == ['unittest']


def test_filter_ignores_if_no_stopwords():
    test_data = ['Important', 'words', 'exist', 'unittest']
    out = filter_stopwords(test_data)
    assert out == test_data


def test_find_indices():
    test_data = ['test', 'this', 'that', 'test']
    word = 'test'
    out = find_indexes(test_data, word)
    assert out == [0, 3]


def test_find_index_with_no_match():
    test_data = ['test', 'this', 'that', 'test']
    word = 'unittest'
    out = find_indexes(test_data, word)
    assert out == []
