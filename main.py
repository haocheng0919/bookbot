import sys
from stats import get_num_words, get_char_counts, get_sorted_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")

    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    sorted_chars = get_sorted_char_list(char_counts)

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

main()
