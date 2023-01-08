def net_amount(statement):
    balance = 0
    items = statement.split()
    for i in range(len(items)):
        if items[i] == 'D':
            balance += int(items[i + 1])
        elif items[i] == 'W':
            balance -= int(items[i + 1])
    return balance


statement_1 = 'D 300 D 300 W 200 D 100'
print(net_amount(statement_1))
