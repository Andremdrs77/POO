def MMC(x, y):
    multiplo = x

    while multiplo % y != 0:
        multiplo += x

    return multiplo


x = int(input("Digite x: "))
y = int(input("Digite y: "))

print(MMC(x, y))
