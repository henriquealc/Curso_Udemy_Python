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
'''Solução feita por mim'''
# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# unirlista= list(zip(lista_a, lista_b))  # Uni as listas A e lista B
# lista_soma = [] # Cria uma nova lista com a soma dos números

# for x, y in unirlista:
#     soma = x + y # Faz a soma dos números 
#     lista_soma.append(soma) # Adiona os números somados na lista
# print(lista_soma)

'''Solução feita pelo professor'''

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# print(list(zip(lista_a, lista_b)))

# # [(x= 1, y=1), (x= 2, y= 2), (x= 3, y= 3), (x= 4, y= 4)] 
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)] # Antes do for a operação que deve ser feita.
# print(lista_soma)


'''
zip - Só une as listas até o tamamho da menor lista (como proposto no exercício)

zip_longest = captura os valores da lista maior.
Usamos ''fillvalue como 0(zero), assim conseguimos capturar os valores restantes
da lista maior, realizando contas, sem obter um erro em nosso programa.
'''

'''Usando o zip_lingest'''

from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]

lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue= 0)]
print(lista_soma)
