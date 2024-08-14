def main():
    file_content = read_file()
    print_report(count_words(file_content), sort_dict(count_chars(file_content)))
    

def read_file():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_chars(text):
    text_lowered = text.lower()
    chars_dict = {}
    for each in text_lowered:
        if each in chars_dict:
            chars_dict[each] += 1
        else:
            chars_dict[each] = 1
    return chars_dict

def sort_dict(dict_unsorted):
    dict_sorted = {}
    for each in sorted(dict_unsorted, key = dict_unsorted.get, reverse=True):
        if each.isalpha():
            dict_sorted[each] = dict_unsorted[each]
    return dict_sorted

def print_report(words, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print()

    print(f"{words} words found in the document")
    
    for each in chars:
        print(f"The '{each}' character was found {chars[each]} times")

    print("--- End report ---") 


main()
