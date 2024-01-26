'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

===================== resultado
lista_soma = [2, 4, 6]
'''
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

unirlista= list(zip(lista_a, lista_b))  # Uni as listas A e lista B
lista_soma = [] # Cria uma nova lista com a soma dos números

for x, y in unirlista:
    soma = x + y # Faz a soma dos números 
    lista_soma.append(soma) # Adiona os números somados na lista
print(lista_soma)
