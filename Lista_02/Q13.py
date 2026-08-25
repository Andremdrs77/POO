def RemoverEspacos(texto):
    return ' '.join(texto.split())

print(RemoverEspacos(input('Digite uma frase:\n')))