# Complete the function to print the last two digits of an interger greater than 9.
def last_two_digits(number):
    if num > 9:
        return num % 100
    else:
        return "numero de un solo dígito"


# Invoke the function with any interger greater than 9.
print(last_two_digits(115))
print(last_two_digits(9))
print(last_two_digits(48))
print(last_two_digits(11154875))
