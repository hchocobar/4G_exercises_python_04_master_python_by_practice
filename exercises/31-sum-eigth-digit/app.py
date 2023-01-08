values = []
for i in range(1000, 3001):
    number = str(i)
    if int(number[0]) % 2 == 0 and int(number[1]) % 2 == 0 and int(number[2]) % 2 == 0 and int(number[3]) % 2 == 0:
        values.append(number)

print(",".join(values))
