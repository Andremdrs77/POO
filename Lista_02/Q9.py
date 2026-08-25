frase = list(map(str, input('Digite uma frase:\n').split()))
print()

for l in range(len(frase)):
    frase[l] = reversed(frase[l])
    print(*frase[l], sep='')