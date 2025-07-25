import sys
from stats import get_book_text
from stats import count_words
from stats import count_characters
from stats import sort_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_link  = sys.argv[1]
        book = get_book_text(book_link)
        sorted_dict = sort_dictionary(count_characters(book))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_link}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(book)} total words")
        print("--------- Character Count -------")
        for entry in sorted_dict:
            if entry["char"].isalpha():
                print(f"{entry["char"]}: {entry["num"]}")
        print("============= END ===============")

main()