string = 'Otávio Miranda'
numero_de_letras = 2

# O join é usado para colocar o ponto entre entre as letras
nova_string = '.'.join([
    # Faz o fatiamento da string
    string[indice: indice + numero_de_letras] # Pega a string e divide as letras em 2 em 2
    for indice in range(0, len(string), numero_de_letras)    
])

print(nova_string)