'''
Empacotamento e desempacotamento de dicionários
'''

# inverte os valores de a e b
# a, b = 1, 2 # aqui o valor de 'a' é 1
# a, b = b, a  # aqui o valor de 'a' passa a ser 2
# print('valor de a:', a, 
#       'Valor de b:', b)


pessoa = {
    #a1       a2
    'nome': 'Aline',
    # b1           b2
    'sobrenome': 'Souza',
}

# (a1, a2), (b1, b2) = pessoa.items()  # As variaveis passam a receber os items que estão no dicionário
# print('a1:',a1, 
#       '\na2:', a2)
# print()
# print('b1:', b1,
#       '\nb2:', b2)
# print()

# for chave, valor in pessoa.items():  # Mostra cada chave e valor que tem no dicionário
#     print(chave, valor)


dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completas = {**pessoa, **dados_pessoa} # Cria um novo dicionário e junta os dois(pessoa e dados_pessoa) em um só
# print(pessoas_completas)


# args e kwargs
# args (já visto mas preciso rever)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)


# argumentos nomeados
# mostro_argumentos_nomeados(nome= 'Joana', qulq = 123) 
# mostro_argumentos_nomeados(**pessoas_completas)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes) 
