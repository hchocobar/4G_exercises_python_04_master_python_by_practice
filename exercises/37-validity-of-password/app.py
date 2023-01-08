import re


def valid_password(pw=''):
    # First: check valid character and length
    if re.fullmatch("[a-zA-Z0-9$#@]{6,12}", pw):
        # Second: check valid character in the four types
        if re.search('[a-z]+', pw) and re.search('[A-Z]+', pw) and re.search('[0-9]+', pw) and re.search('[$#@]+', pw):
            return pw, True
    return pw, False


def split_sequence(sequence):
    value = []
    items = [x for x in sequence.split(',')]
    for p in items:
        value.append(valid_password(p))
    return value


# ABd1234@1,a F1#,2w3E*,2We3345
print(valid_password('ABd1234@1'))
print(valid_password('a F1#'))
print(valid_password('2w3E*'))
print(valid_password('2We3345'))
print(split_sequence('ABd1234@1,a F1#,2w3E*,2We3345'))

