def generate_dict(n):
    result = {}
    for i in range(1, n+1):
        result[i] = i * i
    return result


print(generate_dict(1))
print(generate_dict(4))
print(generate_dict(8))
print(generate_dict(10))
print(generate_dict(15))
