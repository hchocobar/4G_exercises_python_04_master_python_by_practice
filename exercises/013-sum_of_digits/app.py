# Complete the function "digits_sum" so that it prints the sum of a three digit number.
# Implementación 1: standard
def digits_sum(number):
    cadena = str(number)
    suma = 0
    for x in cadena:
        suma += int(x)
    return suma


# Implementación 2: comprehension
def digits_sum_2(number):
    cadena = str(number)
    suma = 0
    suma = sum(int(x) for x in cadena)
    return suma


# Invoke the function with any three-digit-number
# You can try other three-digit numbers if you want
print(digits_sum(123))
print(digits_sum_2(123))
