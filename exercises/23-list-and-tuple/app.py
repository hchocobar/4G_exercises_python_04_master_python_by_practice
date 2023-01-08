def convert_tuple(l):
    return tuple(l)


# 34,67,55,33,12,98
sequencia = input("")
# secuencia = '34,67,55,33,12,98'
lista = list(sequencia.split(','))
print(lista)
print(convert_tuple(lista))
