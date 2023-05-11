'''
split e join com list e str
split - divide uma string (retorna uma lista)
join - une uma string
'''

frase = '    Olha só que  , coisa interessante   '
lista_frases_cruas = frase.split(',') # Separa a frase no ','

lista_frase = [] # cria uma lista
for i, frase in enumerate (lista_frases_cruas):
    lista_frase.append(lista_frases_cruas[i].strip()) # Adiciona a frase na lista e tira os espaços do inicio e fim da frase ao usar o 'split'

# print(lista_frases_cruas)
# print(lista_frase)

frases_unidas = '='.join(lista_frase) # Uni as frases e coloca o '=' entre elas
print(frases_unidas)