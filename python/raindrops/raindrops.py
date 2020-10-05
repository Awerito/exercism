def convert(number):

    factors = [ x for x in [3, 5, 7] if number % x == 0 ]

    raindrop = ''
    if factors:
        for factor in factors:
            if factor == 3:
                raindrop += 'Pling'
            if factor == 5:
                raindrop += 'Plang'
            if factor == 7:
                raindrop += 'Plong'
    else:
        raindrop = str(number)
    return raindrop
