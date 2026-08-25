frase = input('Digite uma frase:\n' )
print()
letras = []

for l in frase:
    letras.append(l)

for l in letras:
    letras.append(letras[0])
    letras.pop(0)
    print(*letras, sep='')