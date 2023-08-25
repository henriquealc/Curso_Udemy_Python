'''
    List comprehension em Python
List comprehension é uma forma rápida 
para criar listas a partir de iteráveis.
'''

import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# print(list(range(10))) # Cria uma lista de 0 a 9.

# lista = []

# # Adiciona os números de 0 a 9 dentro da lista
# for numero in range(10): 
#     lista.append(numero)
# # print(lista)


# Ex de como usar o List comprehension
# Adiciona os números dentro da lista e multiplica cada um deles por 2
lista = [numero * 2 for numero in range(10)]
# print(list(range(10))) # Faz o mapeamento da lista
# print(lista)



'''Mapeamento de dados em list comprehension'''
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # desempacota os precos e aumenta ele em 5%.
    if produto['preco'] > 20 else {**produto} # aumenta o preço caso o preço seja maior que 20
    for produto in produtos
]

# print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
#print(*novos_produtos, sep='\n') # Faz os desempacotamentos dos produtos

# Cria um filtro
# # Filtro o if sempre vem depois do for
# lista = [n for n in range(10) if n < 5]
# print(lista)


''' O que vem na esquerda do for é mapiamento e o que vem a direira
 do for é filtro'''
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto ['preco'] >= 20 and produto['preco'] * 1.05) > 10 
] 

p(novos_produtos)

