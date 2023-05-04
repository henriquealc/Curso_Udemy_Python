"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#........+01234
#........-54321
# string = 'ABCDE' # 5 caracteres (len)
# print(bool([]))  #falsy
# print(lista, type(lista)) 

# lista = [123, True, 'Luiz Otávio', 1.2, []]  # Cria uma lista
# lista[-3] = 'Maria' # Alterando um valor dentro da lista
# print(lista)
# print(lista[2], type(lista[2])) # Verificando o tipo do item 2 na lista


'''Métodos úteis:
    append, insert, pop, del, clear, extend, + 
Create = Criar, read = ler, update = atualizar, delete = deletar
= lista [i] (CRUD)
* CRUD (Create, Read, Update, Delete) é um acrônimo para as maneiras de se operar em informação armazenada,
é um mnemônico para as quatro operações básicas de armazenamento persistente.
'''
#+.......0...1...2...3...4...5...
# lista = [10, 20, 30, 40] # Cria a lista
# lista[2] = 300 # Altera um valor na lista
# del lista[2] # deleta o indice 2 da lista
# print(lista)
# print(lista[2])
# lista.append(50) # Adiciona um valor na lista, este valor adicionado vai para o final da lista]
# lista.pop() # Remove o ultimo item da lista
# lista.append(60)
# lista.append(70)
# lista.pop()
# ultimo_valor = lista.pop(3)
# print(lista, 'removido: ', ultimo_valor)




'''Exemplo de como substituir o elemento de uma lista pelo NOME
do elemento e não pelo indice.'''

# lista = ['Maria', 'José', 'João', 'Pedro']
# lista[lista.index('José')] = 'Joana'
# print(lista)  # ['Maria', 'Joana', 'João', 'Pedro']



 

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#........0...1...2...3
# lista = [10, 20, 30, 40]
# lista.append('Luiz') # Adiciona o nome 'Luiz' na lista
# nome = lista.pop() # Pega o último elemento para poder fazer algo com ele
# lista.append(1233) # Adiciona os números na lista
# del lista[-1] # Deleta o último item da lista
# #lista.clear() # Limpa toda a lista
# lista.insert(100, 5) # Adiona um item na lista no local escolhido.
# print(lista[4])




'''
Métodos úteis:
    extend - estende a lista
    + - concatena listas
'''


# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b) # extende a lista 'a' com os itens da lista 'b'
# print(lista_a)


'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

# lista_a = ['Luiz', 'Maria', 1, True, 1.2]

# lista_b = lista_a.copy() # Copia a lista 'a'

# lista_a[0] = 'Qualquer coisa' # Substitui o primeiro item da lista por 'Qualquer coisa'
# print(lista_a)
# print(lista_b)