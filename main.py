"""
Main module to use the functionality using manual command input.
"""
from book_search_app.core.parser import file_parser
from book_search_app.core.query import search_query


if __name__ == '__main__':
    filename = 'data/data.json'
    indexed_map, summary_map = file_parser(filepath=filename)
    while True:
        query = input("Provide the query to search: ")
        k = 5
        doc_ids = search_query(query, indexed_map)
        print(doc_ids)
        for item in doc_ids[:5]:
            print(summary_map[item])
