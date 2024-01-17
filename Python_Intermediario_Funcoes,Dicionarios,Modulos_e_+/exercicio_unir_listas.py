# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# min - minimo , max - maximo

# def zipper(l1, l2):
#     intervalo_maximo = min(len(l1), len(l2)) # Percorre as listas e ver qual é a menor
#     return [(l1[i], l2[i]) for i in range(intervalo_maximo)] # retorna uma tupla com os nomes dos estados e a sigla
#     # print(min(1, 2))
#     # print(min(200, 150, 1)) # Mostra o valor minimo dessa lista

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(l1, l2))

'''Outro modo de fazer a mesma coisa'''
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2))) # Zip é uma função que ja exite no python permite combinar elementos de duas ou mais listas em uma única estrutura de dados
print(list(zip_longest(l1, l2, fillvalue= 'SEM VALOR'))) # zip_longest usa a lista maior primeiro

