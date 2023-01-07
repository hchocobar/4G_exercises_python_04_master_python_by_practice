def convert_tuple(lista):
    return tuple(lista)


# 34,67,55,33,12,98
sequencia = input("Ingrese una secuancia de números separados por comas")
lista = list(sequencia.split(','))
print(lista)
print(convert_tuple(lista))
