def number_of_words(text):
    words = text.split()
    return len(words)


def character_count_per_letter(text):
    letter_counts = {}
    for letter in text:
        check_letter = letter.lower()
        if check_letter in letter_counts:
            letter_counts[check_letter] += 1
        else:
            letter_counts[check_letter] = 1
            
    return letter_counts

def sort_on(items):
    return items["num"]

def get_sorted_character_counts(count_dictionary):
    sorted_char_counts = []
    for key, item in count_dictionary.items():
        if key.isalpha():
            sorted_char_counts.append({"letter": key, "num": item})

    sorted_counts = sorted(sorted_char_counts, reverse=True, key=sort_on)
    return sorted_counts
