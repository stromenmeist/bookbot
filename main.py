import sys

from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(book_path):

    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()
    

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sort_characters_by_count(character_count):
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()