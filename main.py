from stats import number_of_words, character_count_per_letter, get_sorted_character_counts

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

def main():
    bookpath = 'books/frankenstein.txt'
    bookText = get_book_text(bookpath)    
    num_words = number_of_words(bookText)    
    char_counts = character_count_per_letter(bookText)    
    sorted_char_counts = get_sorted_character_counts(char_counts)    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_char_counts:
        print(f"{letter['letter']}: {letter['num']}")    
    print("============= END ===============")
    
    
    
    
main()
