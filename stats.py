def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_on(item):
    # helper function for sorting by count
    return item["num"]


def get_sorted_char_list(char_counts):
    # convert dict → list of {"char": ..., "num": ...}
    sorted_list = []
    for char, num in char_counts.items():
        if char.isalpha():  # only include alphabetic characters
            sorted_list.append({"char": char, "num": num})

    # sort from greatest to least by "num"
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
