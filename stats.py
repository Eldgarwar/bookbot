def count_words(text):
    words = text.split()
    return len(words)

def count_all_characters(text):
    """
    Counts each individual character in the provided text, including
    letters, numbers, symbols, spaces, and any other character.
    Returns a dictionary with character counts.
    """
    text = text.lower()
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def print_character_counts(text):
    """
    Prints the count for each unique character in the provided text.
    """
    character_counts = count_all_characters(text)
    # The sorted() function ensures consistent output order.
    for char, count in sorted(character_counts.items()):
        print(f"'{char}': {count}")

