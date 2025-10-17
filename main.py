from stats import number_of_words

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

def main():
    bookText = get_book_text('books/frankenstein.txt')
    # print(bookText)
    num_words = number_of_words(bookText)
    print(f"Found {num_words} total words")
    
    

main()
