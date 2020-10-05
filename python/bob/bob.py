def response(hey_bob):
    
    if not hey_bob or hey_bob.isspace():
        return "Fine. Be that way!"

    if hey_bob.isupper():
        if '?' == hey_bob.strip()[-1]:
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
        
    if '?' == hey_bob.strip()[-1]:
        return "Sure."

    return "Whatever."
