def get_book_text(filepath): 
	with open(filepath) as f:
		return f.read()

def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	char_counts = {}
	text = text.lower()

	for ch in text:
		if ch in char_counts:
			char_counts[ch] += 1
		else: 
			char_counts[ch] = 1
	return char_counts

def sort_on(dict_item):
	"""Helper function to sort by the 'num' key"""
	return dict_item["num"]

def sort_char_dict(char_dict):
	"""Convert character dictionary to sorted list of dictionaries"""
	char_list = []
	for char, count in char_dict.items():
		if char.isalpha():  # Only include alphabetical characters
			char_list.append({"char": char, "num": count})
	
	# Sort the list by count (greatest to least)
	char_list.sort(reverse=True, key=sort_on)
	return char_list


