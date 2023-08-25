'''
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.
'''

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# listanum = [4, 32, 1, 34, 5, 6, 6, 21]
# listanum.sort(reverse=True) # coloca a listanum em ordem reversa

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key= lambda item: item['nome']) # coloca os nomes em ordem
l2 = sorted(lista, key= lambda item: item ['sobrenome']) # coloca em ordem pelos sobrenomes

print('Lista em ordem pelos nomes:', end='\n')
exibir(l1)

print('Lista em ordem pelos sobrenomes:', end='\n')
exibir(l2)