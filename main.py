def get_book_text(file_path):
    """
    Takes a filepath as input and returns the contents of the file as a string.
    """
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
    
def main():
    print(get_book_text("./books/frankenstein.txt"))

main()