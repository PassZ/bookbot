import sys
from stats import get_number_of_words, get_character_counts


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book = ""
    book_text = ""

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = get_number_of_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    get_character_counts(book_text)


if __name__ == "__main__":
    main()
