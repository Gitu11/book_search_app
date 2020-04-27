"""
Helper module to be used for core functionality.
"""

STOP_WORDS = {'before', "you're", 'his', 'they', 'but', 'on', 'having', 'which', 'them', 'under', 'such', 'the',
              'because', 'it', 'an', 'up', "he's", 'who', 'about', "doesn't", "they'd", 'was', "we're", 'have', 'nor',
              'then', 'has', 'themselves', 'any', 'once', 'into', 'ought', "mustn't", 'cannot', 'more', "when's",
              "she'd", 'where', "wouldn't", 'why', 'oursourselves', 'through', "here's", 'off', 'that', 'our', 'other',
              'very', "couldn't", 'been', 'itself', "she's", 'there', "don't", 'same', 'whom', 'does', "you've", 'she',
              "i've", 'below', 'when', 'these', "they're", 'out', 'doing', 'how', 'your', "it's", 'with', 'yourself',
              "we'd", 'myself', 'from', 'is', 'her', 'could', 'by', 'theirs', 'be', 'of', 'above', 'than', 'after',
              'if', 'he', 'during', 'not', "how's", 'own', 'you', 'would', "i'd", 'each', 'had', "she'll", "aren't",
              'until', 'i', "we've", 'so', "didn't", "he'd", "weren't", 'what', "why's", "we'll", 'again', 'do',
              'further', "let's", "you'll", 'we', 'few', 'am', "they'll", 'their', "haven't", "there's", "isn't",
              'only', "what's", 'most', 'to', 'both', 'yours', 'at', 'those', 'while', 'being', 'yourselves', "they've",
              'himself', 'hers', 'its', 'should', 'as', 'all', 'my', "that's", 'herself', 'no', "you'd", 'between',
              'down', "hasn't", "who's", 'were', 'against', "hadn't", 'or', "he'll", 'are', "won't", 'this', 'did',
              'him', 'and', "where's", 'here', 'for', "shan't", 'a', "wasn't", "shouldn't", 'some', 'too', "i'll", 'me',
              'over', "i'm", "can't", 'in'}


def filter_stopwords(wordlist: list) -> list:
    """
    Takes list of words as input and filters out the stop words.

    :param wordlist:
    :return:  filtered list of words
    """
    return list(filter(lambda x: x.lower() not in STOP_WORDS, wordlist))


def find_indexes(wordlist: list, word) -> list:
    """
    Returns the list of indexes where the word matches in the wordlist.

    :param wordlist:
    :param word:
    :return:
    """
    return [index for index, value in enumerate(wordlist) if word == value]
