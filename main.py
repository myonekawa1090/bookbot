import sys
from stats import get_character_count, sort_character_count, get_book_words

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    num_words = get_character_count(book_path)
    # Filter out non-alphabetical words
    num_words = {word: count for word, count in num_words.items() if word.isalpha()}
    sorted_list = sort_character_count(num_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_words(book_path)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_list:
        print(f"{char}: {count}")
    print("============= END ===============")