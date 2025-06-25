def number_of_words(text):
    """
    Takes a string and returns the number of words in it.
    """
    return len(text.split())

def character_count(text):
    """
    Takes a string and returns the number of times each character appears in it, including symbols and whitespace after converting to lowercase.
    """
    
    text = text.lower()
    chars = {}
    
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars