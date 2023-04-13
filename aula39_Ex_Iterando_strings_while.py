'''
Iterando strings com while
'''


nome = input('Informe seu nome: ')  # Recebe o nome 

novo_nome = '' 
cont = 0  # Faz o indice começar em '0'
while cont < len(nome):  # Conta quantas letras a no nome
    letra = nome[cont]  # Recebe quantas letras a no nome
    novo_nome += f'*{letra}' # inseri o '*' entre as letras
    cont += 1  # soma as letras no nome

novo_nome += '*' # inseri o '*' no final do nome 
print(novo_nome)
print(f'Seu nome contém {len(nome)} letras.')