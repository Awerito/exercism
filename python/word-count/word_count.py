def get_words(sentence):

    clean_sentence = sentence.lower()
    clean_sentence = clean_sentence.replace(',', ' ')
    clean_sentence = clean_sentence.replace('_', ' ')
    chars = '".;:!?@#$%^&*'

    for char in chars:
        clean_sentence = clean_sentence.replace(char, '')

    clean_sentence = clean_sentence.split()
    words = []
    for word in clean_sentence:
        if word.startswith("'") or word.endswith("'"):
            word = word.replace("'", '')
        words.append(word)
    words.sort()
    return words
    
    
def count_words(sentence):

    words = get_words(sentence)
    counter = {word: words.count(word) for word in words}
    return counter
