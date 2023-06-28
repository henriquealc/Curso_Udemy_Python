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

pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Ferreira',
    'idade': 100,
}

# pessoa.setdefault('idade', 0)
# print(len(pessoa)) # Retorna quantas chaves tem no dicionário
# print(list(pessoa.keys())) # Retorna somente as chaves
# print(list(pessoa.values())) # Retorna apenas os valores
# print(list(pessoa.items())) # Retorna chaves e valores do dicionário

# for valor in pessoa.values(): # Retorna apenas os valores de cada chave
#     print(valor)

# for chave, valor in pessoa.items(): # Retorna chaves e valores 
#     print(chave, valor)
