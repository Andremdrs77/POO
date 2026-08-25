for c in range(1, 11):
    print(c, end=' ')
    pares = []
    for i in range(1, c + 1):
        if i % 2 == 0:
            pares.append(i)
    print(*pares, sep=' ')