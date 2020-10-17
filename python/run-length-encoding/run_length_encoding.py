def decode(string):
    if string:
        decode = ''
        index  = 0
        for i, letter in enumerate(string):
            if letter.isalpha() or letter == ' ':
                if string[index:i]:
                    decode += letter * int(string[index:i])
                else:
                    decode += letter
                index = i + 1
        return decode
    return ''


def encode(string):

    if string:
        sub_strings = []
        index = 0
        length = len(string) - 1
        for i, j, z in zip(string[:-1], string[1:], range(length)):
            if not i == j:
                sub_strings.append(string[index:z + 1])
                index = z + 1
        sub_strings.append(string[index:])

        encode = ''
        for word in sub_strings:
            count = len(word)
            encode += str(count) + word[0] if not count == 1 else word[0]

        return encode
    return ''
