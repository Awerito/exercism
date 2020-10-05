def is_valid(isbn):
    
    if isbn:
        digits = [int(x) for x in isbn if x.isdigit()]

        if isbn.lower()[len(isbn) - 1] == 'x':
            digits.append(10)

        if len(digits) == 10:
            modulo = 0
            for i, digit in enumerate(digits):
                modulo += digit * (10 - i)
            
            return modulo % 11 == 0

    return False
