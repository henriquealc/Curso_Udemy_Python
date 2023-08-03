# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y)) # Adiciona na lista e cria uma tupla para suportar 2 valores

'''Usando o list comprehension para fazer a mesma coisa do codigo acima'''
lista = [
    (x, y) # Cria uma tupla para que tenha 2 números em 1 indice da lista
    for x in range(3)
    for y in range(3)
]

# lista = [
#     [letra for letra in 'Luiz']
#     for x in range(3)
# ]

print(lista)