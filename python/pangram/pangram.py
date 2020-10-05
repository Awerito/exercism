def is_pangram(sentence):
    
    sentence = set([x for x in sentence.lower() if x.isalpha()])
    return len(sentence) == 26
