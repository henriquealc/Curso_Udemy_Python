"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#........+01234
#........-54321
string = 'ABCDE' # 5 caracteres (len)
# print(bool([]))  #falsy
# print(lista, type(lista)) 

lista = [123, True, 'Luiz Otávio', 1.2, []]  # Cria uma lista
lista[-3] = 'Maria' # Alterando um valor dentro da lista
print(lista)
print(lista[2], type(lista[2])) # Verificando o tipo do item 2 na lista