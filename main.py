import sys
from stats import get_book_text, count_words, count_characters, sort_char_dict

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line arguments
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Get book text
    book_text = get_book_text(book_path)
    
    # Count words
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Count characters and sort them
    char_counts = count_characters(book_text)
    sorted_chars = sort_char_dict(char_counts)
    
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ==============")

if __name__ == "__main__":
    main()