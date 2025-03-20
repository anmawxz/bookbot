def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    result = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in result:
            result[char_lower] = 1
        else:
            result[char_lower] += 1
    return result

def sort_on(d):
    return d[1]

def print_report(path_to_file, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    is_alpha = lambda x : x.isalpha()
    characters_alphabet = {
        k:v for (k,v) in sorted(character_count.items(), key=sort_on, reverse=True)
        if is_alpha(k)
    }
    for char in characters_alphabet:
        print(f"{char}: {character_count[char]}")

    print("============= END ===============")