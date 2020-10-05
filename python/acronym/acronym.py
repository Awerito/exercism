def abbreviate(words):

    words = words.replace("-", " ")
    words = words.replace("_", " ")
    clean_words = words.split()
    return ''.join([word[0].upper() for word in clean_words])
