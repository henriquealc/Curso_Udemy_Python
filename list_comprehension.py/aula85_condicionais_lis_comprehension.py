'''
Condicionais list comprehenfion
'''

def espaco():
    print('-' * 50)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Faz um mapiamento na lista 'numeros' e cria uma lista apenas com os numeros maiores do que 5
# Os if's são responsaveis por filtrar
novos_numeros = [numero for numero in numeros if numero > 5]  # Cria uma nova lista e coloca apenas os números maiores que 5 
impares = [numero for numero in numeros if numero % 2 != 0] # Cria uma lista e coloca os valores impares que vem da lista 'numeros'
pares = [numero for numero in numeros if numero % 2 == 0] # Cria uma lista e coloca os valores pares que vem da lista 'numeros'

# Se numeros forem diferente de 6 eles continuam com o mesmo valor, se não são alterados para 600
# O for quer dizer que é para cada números em pares
# Se usar um if depois da variavel estara usando um operados ternario
outro_if = [
    numero 
    if numero != 6 else 600
    for numero in pares            
]


print('Lista com números:', numeros)
espaco()
print('Números maiores que 5:', novos_numeros)
espaco()
print('Números impares:',impares)
espaco()
print('Números pares:', pares)
espaco()
print('Substitui o número 6 por 600:', outro_if)
espaco()