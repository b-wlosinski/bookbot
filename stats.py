def get_book_text(book, encoding='utf-8-sig', newline=''):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(path):
    p = path
    text = get_book_text(p)
    num_words = len(text.split())
    return num_words

def get_char_count(path):
    p = path
    num_words = get_num_words(path)
    letter_count = {}
    text = get_book_text(p).lower()
    words = text.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter in letter_count:
                new_letter_count = letter_count[letter] + 1
                letter_count.update({letter: new_letter_count})
            else:
                letter_count.update({letter: 1})
    del letter_count["\ufeff"]
    return letter_count

def sort_letters(items):
    return items["num"]

def report_characters(letter_count):
    characters = []
    for key, value in letter_count.items():
        if key.isalpha():
            characters.append({"char": key, "num": value})
    characters.sort(reverse=True,key=sort_letters)
    return characters