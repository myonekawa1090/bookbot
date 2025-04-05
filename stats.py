def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        text = f.read()
    return text

def get_book_words(book_path: str) -> list:
    text = get_book_text(book_path)
    words = text.split()
    return len(words)

def get_character_count(book_path: str) -> dict:
    text = get_book_text(book_path).lower()
    character_counts = {}
    for char in text:
        if char not in character_counts:
            character_counts[char] = 0
        character_counts[char] += 1
    return character_counts

def sort_character_count(character_counts: dict) -> list:
    sorted_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts