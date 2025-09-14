from stats import word_count, character_count, character_count_sorted

def practice():
    
    def get_book_text(filePath):       
        with open(filePath) as f:
            contents = f.read()           
        return contents
    
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = word_count(text)
    character_counted = character_count(text)
    characters_sorted = character_count_sorted(character_counted)
    
    # def character_count_sorted(text):
        
    #     char_list = list(text.items())
    #     print(char_list)
    #     sorted_list = sorted(char_list, key=lambda i: i[1], reverse=True)
    #     return sorted_list
    
    # print(character_count_sorted())
    
    def print_pretty(path, num_words, characters_sorted):
        char_dict = dict(characters_sorted)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for key, value in char_dict.items():
            print(f"{key}: {value}")
        print("============= END ===============")
    
    print_pretty(path, num_words, characters_sorted)

practice()