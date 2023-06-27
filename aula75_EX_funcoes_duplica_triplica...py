'''
Exercìcio
Crie funções que duplica, triplica e quadruplicam
o número recebido como parâmetro.
'''


# def duplica(num):
#     return num * 2

# def triplica(num):
#     return num * 3

# def quadruplica(num):
#     return num * 4

# print(duplica(2))
# print(triplica(3))
# print(quadruplica(4))



# valor = int(input('Digite um valor para duplica-lo, triplica-lo e quadruplica-lo: '))

# def duplica(valor):
#     return valor * 2
# def triplica(valor):
#     return valor * 3
# def quadruplicar(valor):
#     return valor * 4

# print(f'O valor duplicado é', duplica(valor),
#       '\nO valor triplicado é', triplica(valor),
#     '\nO valor quadruplicado é', quadruplicar(valor))



'''Maneira feita pelo professor'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))