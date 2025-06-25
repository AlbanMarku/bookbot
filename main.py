import sys
from stats import character_count, sorted_list
def get_book_text(file_path):
    """
    Takes a filepath as input and returns the contents of the file as a string.
    """
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
    
    
def main():
    if len(sys.argv) > 1:
        book = sys.argv[1]
        book_text = get_book_text(book)
        chars = character_count(book_text)
        sorted_list(chars, book, book_text)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    

main()