def get_word_count(text):
    return len(text.split())
    
def get_char_occurances(text):
    chars = {}
    for char in text:
        char = char.lower()
        if chars.get(char) == None:
            chars[char] = 0
        chars[char] += 1
    return chars

