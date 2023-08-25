numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x] # Coloca tudo em uma lista só
print(numeros)
print()
print('Flat:', flat)