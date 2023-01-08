def divisable_binary(sequence):
    divisible_by_5 = []
    items = sequence.split(',')
    for n in items:
        number = int(n, 2)  # convierte el string (binario) a entero decimal
        if number % 5 == 0:
            divisible_by_5.append(n)
    # return divisible_by_5
    return ','.join(divisible_by_5)


print(divisable_binary('0100,0011,1010,1001,1111'))
