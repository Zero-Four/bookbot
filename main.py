from stats import word_count, character_count, character_count_sorted, print_pretty
import sys

def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
        
    path_to_book = sys.argv[1]
        
    def get_book_text(path_to_book):       
        with open(path_to_book) as f:
            contents = f.read()           
        return contents
    
    
    book_as_str = get_book_text(path_to_book)
    book_count = word_count(book_as_str)
    #character_check = ""
    #print(book_as_str)
    #print(book_count)
    

    character_counted = character_count(book_as_str)
    
    #print(character_counted)
    
    # characters_sorted = {}
    characters_sorted = character_count_sorted(character_counted)
    
    #print(characters_sorted)
    print_pretty(path_to_book, book_count, characters_sorted)
    
    

main()





