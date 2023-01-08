def letters_and_digits(text):
    my_dict = {"digits": 0, "letters": 0}
    for char in text:
        if char.isdigit():
            my_dict["digits"] += 1
        elif char.isalpha():
            my_dict["letters"] += 1
        else:
            pass
    return "LETTERS {} DIGITS {}".format(my_dict['letters'], my_dict['digits'])


song = 'Released: 1971 - Artist: John Lennon'
print(letters_and_digits(song))
