from contextlib import asynccontextmanager


def get_number_of_words(text):
    return len(text.split())


def get_character_counts(text):
    char_counts = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1

    # Sort the dictionary highest to lowest
    char_counts = dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))

    for char in char_counts:
        print(f"{char}: {char_counts[char]}")

    return char_counts
