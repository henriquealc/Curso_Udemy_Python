'''
Higher Order Functions
Funções de primeira classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


print(saudacao('Ola', 'Barry'))
print(saudacao('Ola', 'Flash'))