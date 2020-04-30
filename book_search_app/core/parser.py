"""
Parser module to parse the complete data and build invert index.
"""
import json
from collections import defaultdict

from book_search_app.utils.helper import filter_stopwords, find_indexes


def file_parser(filepath: str) -> (dict, dict):
    """
    Takes the file path to read for parsing and returns the invert index of the data.
    Also, returns the summary_id mapping to actual summary.

    :param filepath:
    :return:
    """
    with open(filepath) as fp:
        filedata = json.load(fp)

    indexed_map = defaultdict(list)
    for summary_item in filedata['summaries']:
        # Sanitize the data
        summary_item['summary'] = sanitize_data(summary_item['summary'])

        word_list = filter_stopwords(summary_item['summary'].split())
        processed_words = set()
        for word in word_list:
            if word not in processed_words:
                indexed_map[word].append([summary_item['id'], find_indexes(word_list, word)])
                processed_words.add(word)

    summary_map = {summary['id']: {'summary': summary['summary']} for summary in filedata['summaries']}
    return indexed_map, summary_map


def sanitize_data(sentence):
    """
    Removes replaces the unwanted characters

    :param sentence:
    :return:
    """
    sentence = sentence.replace("\xa0", " ")
    sentence = sentence.replace("\u00a0", " ")
    sentence = sentence.replace("The Book in Three Sentences: ", "")
    sentence = sentence.replace("\u201c", '"').replace("\u201d", '"')
    sentence = sentence.replace("\u2019", "'")
    sentence = sentence.replace(".", "")
    return sentence
