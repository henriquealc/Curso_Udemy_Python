'''
Exemplos de como usar o list comprehension
'''

def divisaoFn(x, y):
    return x / y

def multiplicaFn(x, y):
    return x * y

def potenciaçãoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]

# Cria uma nova lista a partir da lista 'numeros'
# Faz um mapiamento e NÃO altera a lista 'numero'
# novos_numeros = [numero for numero in numeros]

'''Feito com o uso da função def'''
divisao = [divisaoFn (numero, 2) for numero in numeros]
multiplica = [multiplicaFn (numero, 2) for numero in numeros]
quadrado = [potenciaçãoFn (numero, 2) for numero in numeros]


'''Feito sem o uso da função'''
# divisao = [numero / 2 for numero in numeros]
# multiplica = [numero * 2 for numero in numeros]
# quadrado = [numero ** 2 for numero in numeros]

print('Lista:',numeros)
print('Divisão:', divisao)
print('Multiplicação:', multiplica)
print('Quadrado:', quadrado)
# print(novos_numeros)
