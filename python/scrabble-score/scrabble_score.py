def score(word):

    clean_word = word.upper()
    table_points = {
            1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
            2: ['D', 'G'],
            3: ['B', 'C', 'M', 'P'],
            4: ['F', 'H', 'V', 'W', 'Y'],
            5: ['K'],
            8: ['J', 'X'],
            10: ['Q', 'Z']
    }

    points = 0
    for key, letters in table_points.items():
        for letter in letters:
            points += key * clean_word.count(letter)

    return points
