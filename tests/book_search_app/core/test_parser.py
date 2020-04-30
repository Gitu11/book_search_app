"""
Test module to write unit tests for the parser module.
"""
from book_search_app.core.parser import sanitize_data


def test_removes_unicode_characters():
    test_sentence = 'This is\xa0my test\u00a0sentence'
    out = sanitize_data(test_sentence)
    assert out == 'This is my test sentence'


def test_remove_initial_prelogue():
    test_sentence = 'The Book in Three Sentences: This is my test sentence'
    out = sanitize_data(test_sentence)
    assert out == 'This is my test sentence'


def test_removes_full_stop():
    test_sentence = 'This is my test sentence.'
    out = sanitize_data(test_sentence)
    assert out == 'This is my test sentence'
