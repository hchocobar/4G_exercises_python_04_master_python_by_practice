def generate_matrix(x, y):
    matrix = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(j * i)
        matrix.append(row)
    return matrix

print(generate_matrix(3, 5))
print(generate_matrix(8, 11))
