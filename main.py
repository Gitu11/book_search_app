"""
Main module to use the functionality using manual command input.
"""
from book_search_app.core.parser import file_parser, sanitize_data
from book_search_app.core.query import search_query


if __name__ == '__main__':
    filename = 'data/data.json'
    indexed_map, summary_map = file_parser(filepath=filename)
    while True:
        query = input("Provide the query to search: ")
        k = int(input("How many max results you want: "))
        doc_ids = search_query(query, indexed_map)
        print(doc_ids)
        for item in doc_ids[:k]:
            summary_map[item]['summary'] = sanitize_data(summary_map[item]['summary'])
            print(summary_map[item]['summary'])
