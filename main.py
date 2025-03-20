# from stats import count_words
# import sys

# def main():
#     file_content = read_file()
#     print_report(count_words(file_content), sort_dict(count_chars(file_content)))
    

# def read_file():
#     with open("books/frankenstein.txt") as f:
#         return f.read()

# def count_chars(text):
#     text_lowered = text.lower()
#     chars_dict = {}
#     for each in text_lowered:
#         if each in chars_dict:
#             chars_dict[each] += 1
#         else:
#             chars_dict[each] = 1
#     return chars_dict

# def sort_dict(dict_unsorted):
#     dict_sorted = {}
#     for each in sorted(dict_unsorted, key = dict_unsorted.get, reverse=True):
#         if each.isalpha():
#             dict_sorted[each] = dict_unsorted[each]
#     return dict_sorted

# def print_report(words, chars):
#     print("--- Begin report of books/frankenstein.txt ---")
#     print()

#     print(f"{words} words found in the document")
    
#     for each in chars:
#         print(f"The '{each}' character was found {chars[each]} times")

#     print("--- End report ---") 


# main()


import sys
from stats import count_words, count_characters, print_report

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        print_report(path_to_file, word_count, char_count)

main()