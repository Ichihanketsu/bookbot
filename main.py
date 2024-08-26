def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = count_words(text)
    # print(f"{words} words found in the book.")
    characters = count_characters(text)
    # print(f"{characters} characters found in the book.")
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    generate_report(book_path, words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.lower().split()
    character_dict = {}
    for words in words:
        for char in words:
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    return character_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def generate_report(directory, word_count, character_count):

    print(f"--- Begin report of {directory} ---")
    print(f"{word_count} words found in the document\n")


    for item in character_count:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()
