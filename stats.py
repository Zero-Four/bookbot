
def word_count(book_contents):
    
    content_list = book_contents.split()
    num_words = ""
    num_words = str(len(content_list))
    #print(num_words + " words found in the document" )
    return num_words

def character_count(text):
    lowercase_text = text.lower()
    chars_in_text = {}
    for k in lowercase_text:
        if k in chars_in_text:
            chars_in_text[k] += 1
        else:
            chars_in_text[k] = 1                 
    return chars_in_text

def character_count_sorted(char_count):
    char_list = list(char_count.items())
    #print(char_list)
    sorted_list = sorted(char_list, key=lambda i: i[1], reverse=True)
    return sorted_list

def print_pretty(path, num_words, characters_sorted):
    char_dict = dict(characters_sorted)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in char_dict.items():
        if key.isalpha() == True:
            print(f"{key}: {value}")
    print("============= END ===============")

# print_pretty(path, num_words, characters_sorted)