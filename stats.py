def count_words(text):
    words = text.split()
    return len(words)

def count_all_characters(text):
    text = text.lower()
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# This helper function is correct and doesn't need to change.
def sort_on(items):
    return items["count"]

# CORRECTED a new name to reflect that it now handles a list of dicts
def print_sorted_character_report(char_list,book_text,book_path):
    """
    Sorts a list of dictionaries by the 'count' key (high to low)
    and prints a report.
    """
    # .sort() works because char_list is a list!
    char_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_list:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

