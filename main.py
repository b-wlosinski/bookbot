import sys
from stats import get_num_words,get_char_count,report_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        num_words = get_num_words(path)
        letter_count = get_char_count(path)
        characters = report_characters(letter_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for c in characters:
            print(c["char"]+": "+ str(c["num"]))
        print("============= END ===============")
main()