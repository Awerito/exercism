def distance(strand_a, strand_b):

    if len(strand_a) == len(strand_b):
        hamming_distance = 0
        for letter_a, letter_b in zip(strand_a, strand_b):
            if not letter_a == letter_b:
                hamming_distance += 1
        return hamming_distance
    else:
        raise ValueError('.+')
