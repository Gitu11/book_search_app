"""
Test module to write unit tests for the parser module.
"""
from book_search_app.core.parser import sanitize_data, file_parser
import json
from unittest.mock import mock_open


test_file_data = {'summaries': [{'id': 0, 'summary': 'This is test data for solving the unit test problems.'}]}


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


def test_parser_indexed_map(mocker):
    mocker.patch("builtins.open")
    mocker.patch.object(json, 'load', return_value=test_file_data)
    indexed_map, summary_map = file_parser('any_random_value')
    assert 'problems' in indexed_map
    assert indexed_map['solving'] == [[0, [2]]]  # After sanitization
    assert len(summary_map) == 1


def test_parser_indexed_map_ignores_stopwords(mocker):
    mocker.patch("builtins.open")
    mocker.patch.object(json, 'load', return_value=test_file_data)
    indexed_map, summary_map = file_parser('any_random_value')
    assert 'This' not in indexed_map
    assert 'is' not in indexed_map
