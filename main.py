from stats import count_words
from stats import count_all_characters
from stats import print_sorted_character_report
import sys

def get_book_text(book_path):
    with open(book_path, "r") as file:
        return file.read()
    
def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = count_words(book_text)

        # 1. Get the dictionary of character counts
        character_counts_dict = count_all_characters(book_text) # returns a dict
        
        # 2. Convert the dictionary into a list of dictionaries
        character_counts_list = []
        for char, count in character_counts_dict.items():
            character_counts_list.append({"char": char, "count": count})
            
        # 3. Pass the LIST to the sorting and printing function
        print_sorted_character_report(character_counts_list,book_text,book_path)

main()