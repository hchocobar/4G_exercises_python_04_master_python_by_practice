# Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
    left_digit = digit // 10 
    righ_digit = digit % 10
    return (left_digit, righ_digit)
   

# Invoke the function with any interger as its argument.
print(two_digits(79))
