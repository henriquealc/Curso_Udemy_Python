'''
Crie uma função que multíplica todos os argumentos
não nomeados recebidos.
Retorne o total para uma variável e mostre o valor
da variável.
'''
# def multiplica(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total

# multi_1 = multiplica(2, 5, 9)
# multi_2 = multiplica(2, 7)
# multi_3 = multiplica(1, 2, 3, 5, 10, 20)
# print('2 * 5 * 9 =', multi_1)
# print('-=' * 25)
# print('2 * 7 =', multi_2)
# print('-=' * 25)
# print('1 * 2 * 3 * 5 * 10 * 20 =', multi_3)




'''
Crie uma função que fala se um número é par ou impar.
Retorne se o número é par ou impar.
'''
# from time import sleep

# while True:
#     def par_impar():    
#         num = int(input('Informe um número para saber se ele é par ou impar: '))
#         if num % 2 == 0:
#             print(f'O número {num} é PAR.')
#         else:
#             print(f'O número {num} é IMPAR.')


#     num = par_impar()

#     sair = input('Deseja sair? [S/N]: ').lower()
#     if sair == 's':       
#         print('-=' * 25)
#         print('Encerrando programa...')
#         sleep(1.0)
#         print('Programa encerrado com sucesso, Obrigado!')
#         break







'''Resolução feita pelo professor'''

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))