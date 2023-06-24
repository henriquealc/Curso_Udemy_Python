'''
args -> Argumentos não nomeados
* -> *args (empacotamento e desempacotamento)
'''

# Lembre-te de desempacotamento

#              x, y|(resto)
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
    # return x + y

def soma (*args):
    total = 0
    for numero in args:
      total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print('Soma 1 + 2 + 3 = ', soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print('Soma 4 + 5 + 6 = ', soma_4_5_6)

soma_2_3 = soma(1, 2)
print('Soma 1 + 2 = ', soma_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print('Resulado da soma de 1 até 7 + 78 + 10 = ', outra_soma)

print('Soma usando a função "sum" =', end=' ')
print(sum(numeros))