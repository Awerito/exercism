def is_isogram(string):
    
    clean_string = [L for L in string.lower() if L.isalpha()]
    clean_string.sort()
    for letter_a, letter_b in zip(clean_string[:-1], clean_string[1:]):
        if letter_a == letter_b:
            return False
    return True
