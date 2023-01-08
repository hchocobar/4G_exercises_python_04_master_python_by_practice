def divisable_binary(text):
    value=[]
    items=[x for x in text.split(',')]
    for p in items:
        intp = int(p, 2)
        if not intp%5:
            value.append(p)

    return (','.join(value))


print(divisable_binary('0100,0011,1010,1001'))
