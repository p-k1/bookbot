from stats import count_words,count_symbols,dictsort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words(get_book_text(sys.argv[1]))
    num_symbols = count_symbols(get_book_text(sys.argv[1]))
    num_sorted = dictsort(num_symbols)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in num_sorted:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["value"]}")
    print("============= END ===============")
main()