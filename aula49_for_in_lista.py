'''
for in com listas
'''
# lista = ['Maria', 'Helena', 'Luiz'] 

# for nome in lista:  # para cada nome em lista 
#     print(nome, type(nome)) # imprimi os nome da lista e seu tipo


'''
Exercício proposto pelo professor:
Exiba os índices da lista
Solução feira por mim 
'''
# num = -1
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# for nome in lista:
#     num += 1
#     print(num, nome, type(nome))



'''Solução feita pelo professor'''

lista = ['Mario', 'José', 'Kvaratskhelia']
lista.append('James')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))