"""
Parser module to parse the complete data and build invert index.
"""
import json
from collections import defaultdict

from book_search_app.utils.helper import filter_stopwords, find_indexes


def file_parser(filepath: str) -> dict:
    """
    Takes the file path to read for parsing and returns the invert index of the data.

    :param filepath:
    :return:
    """
    with open(filepath) as fp:
        filedata = json.load(fp)

    indexed_map = defaultdict(list)
    for summary_item in filedata['summaries']:
        summary_item['summary'] = summary_item['summary'].replace("\xa0", " ")
        word_list = filter_stopwords(summary_item['summary'].split())
        for word in word_list:
            indexed_map[word].append([summary_item['id'], find_indexes(word_list, word)])

    return indexed_map


