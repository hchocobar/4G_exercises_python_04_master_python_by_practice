values = '1,2,3,4,5,6,7,8,9'
numbers = [x for x in values.split(",") if int(x) % 2 != 0]
print(numbers)  # imprime la lista
print(",".join(numbers))  # imprime una cadena separada por ,
