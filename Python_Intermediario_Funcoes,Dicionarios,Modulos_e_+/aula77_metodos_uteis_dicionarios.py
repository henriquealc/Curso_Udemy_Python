'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''

# pessoa = {
#     'nome': 'Henrique',
#     'sobrenome': 'Ferreira',
#     'idade': 100,
# }

# pessoa.setdefault('idade', 0)
# print(len(pessoa)) # Retorna quantas chaves tem no dicionário
# print(list(pessoa.keys())) # Retorna somente as chaves
# print(list(pessoa.values())) # Retorna apenas os valores
# print(list(pessoa.items())) # Retorna chaves e valores do dicionário

# for valor in pessoa.values(): # Retorna apenas os valores de cada chave
#     print(valor)

# for chave, valor in pessoa.items(): # Retorna chaves e valores 
#     print(chave, valor)



'''
EX de copy (copia rasa)
'''

# import copy # importa a copia profunda


# d1 = {
#     'c1': 1,
#     'c2': 2, 
#     'l1': [0, 1, 2],
# }
# d2 = d1.copy()

# # d2 = copy.deepcopy(d1) # copia profunda 

# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(d1)
# print(d2)





p1 = {
    'nome': 'Henrique',
    'sobrenome': 'Ferreira'
}

# print(p1['nome'])
#print(p1.get('nome', 'Não existe')) # se nome NÃO EXISTE no dicionário retorna None

'''pop - Apaga um item com a chave especificada (del)'''
# nome = p1.pop('nome')
# print(nome)
# print(p1) # Retorna o print da lista sem a chave nome



''' popitem - Remove a ultima chave do dicionário'''
# ultima_chave = p1.popitem() 
# print(ultima_chave)
# print(p1)


'''uptade - atualiza o dicionário'''
# Ex 01:
# p1.update({
#     'nome': 'new name',
#     'idade': 30,
# })


#Ex 02:
# p1.update(nome= 'novo nome', idade= 100)


#Ex 03 com tuplas:
# tupla = (('nome', 'novo nome'), ('idade', 190))
# p1.update(tupla)


#Ex 04 com listas:
lista = [['nome', 'novo nome4'], ['idade', 130]]
p1.update(lista)
print(p1)