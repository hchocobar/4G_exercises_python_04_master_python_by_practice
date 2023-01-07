# Complete the function to return the tens digit of a given interger
def tens_digit(number):
    tens = (number % 100) // 10
    return tens


# Invoke the function with any interger.
print(tens_digit(1234))
print(tens_digit(179))
print(tens_digit(465))
print(tens_digit(585))
