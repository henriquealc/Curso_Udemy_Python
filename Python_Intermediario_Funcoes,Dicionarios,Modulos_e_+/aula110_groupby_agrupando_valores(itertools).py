# groupby - agrupando valores (itertools)
from itertools import groupby
'''
EX 01:
'''
# Agrupar palavras por tamanho com a lista não ordenada:


# frutas = ['Kiwi', 'apple', 'banana', 'grape', 'pear', 'orange']
# grupo = groupby(frutas, key= lambda x: len(x)) # Agrupando pelo tamanho(len)

# for chave, gruop in grupo:
#     print(chave, list(gruop)) # O group é um iterador e precisa vir dentro de uma lista




'''
EX 02:
'''
# Agrupa alunos pela sua nota

# alunos = [{'nome': 'Luiz', 'nota': 'A'},
#           {'nome': 'Letícia', 'nota': 'B'},
#           {'nome': 'Fabricio', 'nota': 'A'},
#           {'nome': 'Rosemary', 'nota': 'C'},
#           {'nome': 'Joana', 'nota': 'D'},
#           {'nome': 'João', 'nota': 'A'},
#           {'nome': 'Eduardo', 'nota': 'B'},
#           {'nome':'André', 'nota': 'A'},
#           {'nome':'Anderson', 'nota': 'C'},
# ]

# # Ordena a lista por nota
# def ordena_por_nota(aluno): # Função para usar o sorted abaixo e evitar repetição de cod
#     return aluno['nota']

# alunos_ordenados = sorted(alunos, key=ordena_por_nota) # Recebe a função acima
# grupos = groupby(alunos_ordenados, key=ordena_por_nota) # Separa pelas notas

# for chave, grupo in grupos:
#     print(chave)
#     for aluno in grupo: # Imprime os dicts dos alunos um abaixo do outro
#         print(aluno)

'''
EX 03:
'''
# Agrupar palavras por tamanho com a lista ordenada:


# words = ['kiwi', 'apple', 'banana', 'grape', 'pear', 'orange']  # lista não ordenada de acordo com o tamanho das palavras
# sorted_words = sorted(words, key=lambda w: len(w))  # ordenando pelo tamanho das palavras antes de agrupar

# groups = groupby(sorted_words, key=lambda x: len(x))  # agrupando a lista ordenada

# for key, group in groups:
#     print(key, list(group))


'''
EX 04:
'''
# Agrupar tipos de animais em um dicionário a partir de uma lista com tuplas:


# animals = [
#     ('mammal', 'monkey'),
#     ('mammal', 'elephant'),
#     ('mammal', 'tiger'),
#     ('oviparous', 'eagle'),
#     ('oviparous', 'crocodile'),
#     ('oviparous', 'duck'),
# ]  # a lista animals já está ordenada de acordo com o tipo do animal, então não precisamos fazer a ordenação antes de agrupar


# groups = groupby(animals, lambda i: i[0])  # agrupa pelo primeiro elemento da tupla

# for key, group in groups:
#     animals_dict = {key: list(group)}  # criei um dict com os animais agrupados pelo tipo (mammal (mamíferos) e oviparous (oviparos))
#     print(animals_dict)