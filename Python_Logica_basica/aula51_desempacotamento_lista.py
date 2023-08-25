'''Introdução ao desempacotamento + tuples (tuplas)'''

# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
_, nome2, *_ = ['Maria', 'Helena', 'Luiz'] # Criando uma variavel de resto
print(nome2, _)