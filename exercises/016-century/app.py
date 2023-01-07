# Complete the function to return the respective number of the century
# HINT: You may need to import the math module.
import math

def century(year):
    return math.ceil(year / 100)


# Invoke the function with any given year. 
print(century(1901))
print(century(2011))
print(century(441))
print(century(1781))
