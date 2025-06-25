from stats import number_of_words, character_count
def get_book_text(file_path):
    """
    Takes a filepath as input and returns the contents of the file as a string.
    """
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
    
    
def main():
    # text_content = get_book_text("./books/frankenstein.txt")
    # word_count = number_of_words(text_content)
    # print(f"{word_count} words found in the document")
    print(character_count(get_book_text("./books/frankenstein.txt")))

main()