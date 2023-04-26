# texto = 'Python s2'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i += 1


'''Um exemplo de como usar While'''
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 3

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha({repeticoes}): ')
    
#     repeticoes += 1
# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')


'''Passando em cada uma das letras com for'''
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
    