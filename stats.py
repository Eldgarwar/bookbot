def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    """Return a list of 26 integers with counts for letters a..z in `text`.

    Non-letter characters are ignored. The counts are case-insensitive.

    Example: 'abA!' -> [2,1,0,0,...]
    """
    text = text.lower()
    counts = [0] * 26
    for ch in text:
        if 'a' <= ch <= 'z':
            counts[ord(ch) - ord('a')] += 1
    return counts


def print_character_counts(text):
    """Print counts for letters a..z in the format: "'a': <count>" for each letter."""
    counts = count_characters(text)
    for i, c in enumerate(counts):
        letter = chr(ord('a') + i)
        print(f"'{letter}': {c}")

