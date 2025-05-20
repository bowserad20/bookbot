from stats import *
from sys import argv

def get_book_text(path):
    with open(path) as file:
        return file.read()
    
def get_charMap_str(charMap):
    str = ''
    for char in charMap:
        str += f"{char}: {charMap[char]}\n"
    return str

def pretty(wCount, charMap, path):
    str = f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {wCount} total words
--------- Character Count -------
{get_charMap_str(charMap)}
    """
    print(str)

def main():
    try:
        if (len(argv) < 2): raise Exception('Usage: python3 main.py <path_to_book>')
        path = argv[1]
        content = get_book_text(path)
        pretty(get_word_count(content), get_char_occurances(content), path)
        
    except Exception as e:
        print(e)
        exit(1)
main()

    