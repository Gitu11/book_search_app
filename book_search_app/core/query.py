"""
Query module to add the search logic.
"""
from collections import defaultdict
from book_search_app.utils.helper import filter_stopwords


def search_query(query, indexed_map):
    """
    Finds all occurrences of all the words, ranks the result and returns


    :param query:
    :param indexed_map:
    :return:
    """
    query_word_list = filter_stopwords(query.split())
    word_search_map = defaultdict(list)
    for word in query_word_list:
        if word in indexed_map:
            for item in indexed_map[word]:
                word_search_map[item[0]].append(item[1])
    #print(word_search_map)
    ranked_docs = relevance_ranking(word_search_map)
    return ranked_docs


def relevance_ranking(word_map):
    """
    Determines relevance of summary based on two type of rankings in below order:
        1) How many words were found in the summary
        2) If two had same number of words- which summary had the maximum of minimum finds.

    :param word_map:
    :return:
    """
    rank_map = defaultdict(list)
    for key in word_map:
        num_of_words_matched = len(word_map[key])
        min_times_word_matched = len(min(word_map[key], key=lambda x: len(x)))
        rank_map[key] = (num_of_words_matched, min_times_word_matched)
    return sorted(rank_map.keys(), key=lambda x: (-rank_map[x][0], -rank_map[x][1]))
