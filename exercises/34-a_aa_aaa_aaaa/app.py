def computed_value(number):
    n1 = int("%s" % number)
    n2 = int("%s%s" % (number, number))
    n3 = int("%s%s%s" % (number, number, number))
    n4 = int("%s%s%s%s" % (number, number, number, number))
    total = n1 + n2 + n3 + n4
    my_tuple = (total, n1, n2, n3, n4)
    return my_tuple


print(computed_value(9))
print(computed_value(5))
print(computed_value(25))
