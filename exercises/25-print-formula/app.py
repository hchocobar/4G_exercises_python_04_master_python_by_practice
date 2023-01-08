import math

def print_formula(number):
    q = math.sqrt(2 * 50 * number / 30)
    return math.ceil(q)


print(print_formula(100))
print(print_formula(150))
print(print_formula(180))
