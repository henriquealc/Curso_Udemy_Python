'''
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
'''

# pessoa = {
#     'nome': 'Henrique', 
#     'sobrenome': 'Ferreira',
#     'idade': 21,
#     'altura': 1.71,
#     'endereços':[
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# print(pessoa['nome']) # printa o nome da pessoa que esta no dicionario
# print(pessoa['sobrenome'])
# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])



'''Manipulando chaves e valores em dicionários'''

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Henrique'
# pessoa['nome'] = 'Henrique' # faz a mesma coisa do código acima
pessoa['sobrenome'] = 'Ferreira'

print(pessoa[chave])

# # printa os nomes sem os '[]'
# for chave in pessoa:
#     print(chave, pessoa[chave]) 

pessoa[chave] = 'Marta' # Substitui a o nome que esta na variavel 'chave'
# print(pessoa[chave])

# del pessoa['sobrenome'] # Exclui o sobrenome no dicionário 'pessoa'
print(pessoa)
print(pessoa['nome'])

# Um if simples não para a excessão
# print(pessoa.get('sobrenome')) # Retorna None

# .get tenta obter uma chave, retorna None se a chave não existir
if pessoa.get('sobrenome') is None: 
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
