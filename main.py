def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import num_of_words
from stats import get_characters
from stats import sort_dict

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    
    book_text = get_book_text(book_path)
    word_count = num_of_words(book_text)
    char_count = get_characters(book_text)
    sorted_dict = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_dict:
        if pair["char"].isalpha() == True:
            print(f"{pair["char"]}: {pair["num"]}")


main()