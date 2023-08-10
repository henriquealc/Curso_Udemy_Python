#Generator expression, iterables e iterators em Python
# iterator = entrega um valor por vez

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator)) 
# print(next(iterator)) 


'''Generator'''

import sys

lista = [ n for n in range(100)]
generator = (n for n in range(100)) # Consome menos memoria no computador

# print(lista)
print()
print(sys.getsizeof(lista)) # Mostra o tamanho da lista em byts
print(sys.getsizeof(generator))
print(generator)

# for n in generator:
#     print(n)