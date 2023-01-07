# Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(number):
    # Your code here
    swap_str = str(number)
    swap_reverse = swap_str[::-1]
    swap_integer = int(swap_reverse)
    return swap_integer


# Invoke the function with any two digit interger as its argument
print(swap_digits(30))
print(swap_digits(79))
