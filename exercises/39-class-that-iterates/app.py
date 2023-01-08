# Defino una función, que es mas apropiado que una clase
def divisible_seven(number):
    my_list = []
    for n in range(0, number+1, 7):
        my_list.append(n)
    return my_list


print(divisible_seven(0))  # Salida: [0]
print(divisible_seven(3))  # Salida: [0]
print(divisible_seven(7))  # Salida: [0, 7]
print(divisible_seven(21))  # Salida: [0, 7, 14, 21]
print(divisible_seven(100))  # Salida: [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
