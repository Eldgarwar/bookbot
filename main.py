from stats import count_words
from stats import print_character_counts

def get_book_text(book_path):
    with open(book_path, "r") as file:
        return file.read()
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    print_character_counts(book_text)

main()