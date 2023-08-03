# Dicionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritório',
}


'''O for abaixo faz a mesma coisa que o 'dc' '''
# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor.upper() # Deve apagar o 'upper' caso for usar o outro if 
    if isinstance(valor, str) else valor # Se for do tipo str coloca em maiunsculo, se não ele coloca apenas o valor
    # if isinstance(valor, (int, float)) else valor.upper() # Faz ao contrario do if a cima, a tupla é passada caso deseje verificar mais valores
    for chave, valor in produto.items()
    if chave != 'categoria' # Tira a categoria
}




lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

# Consegui converter uma lista em um dicionario quando tem valor e chave
# print(dict(lista)) 

# print(dc)

s1 = {2 ** i for i in range(10)} # Faz a conta de 2 elevado ao numero
# print(set(range(10))) # Tn pode ser assim, gera um set com números de 0 a 9
print(s1)