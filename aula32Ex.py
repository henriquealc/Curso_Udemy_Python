"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input('Informe um número inteiro: ')

# if num.isdigit():
#     num = int(num)
#     if num % 2 == 0:
#         print(f'O número {num} é par.')
#     else:
#         print(f'O número {num} é impar.')
# else:
#     print('Informe um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

 # Maneira feita por mim
# hora = input('Informe a hora atual: ')

# if hora.isdigit():
#     hora = int(hora)
#     if hora <= 11:
#         print('Bom dia!')
#     elif hora <= 17:
#         print('Boa tarde!')
#     else:
#         print('Boa noite!')
# else:
#     print('Informe apenas números')


'''MANEIRA FEITA PELO PRFESSOR'''

# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
# except:
#     print('Não reconheço essa hora.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''MANEIRA FEITA POR MIM'''

# nome = input('Informe o seu primeiro nome: ')


# if len(nome) == 4:
#     print('Seu nome é curto!')
# elif len(nome) < 6:
#     print('Seu nome é normal!')
# else:
#     print('Seu nome é muito grande!')

''''''''

# nome = input('Informe o seu nome: ')

# try: 
#     if nome.isdigit():
#         print('Digite apenas letras!')
#     elif len(nome) == 4:  # len - usado para contar quantas letras tem no nome
#         print('Seu nome é curto!')
#     elif len(nome) <= 6:
#         print('Seu nome é normal!')
#     elif len(nome) > 6:
#         print('Seu nome é muito grande!')
# except:
#     print('Informe um nome valido.')


'''MANEIRA FEITA PELO PROFESSOR'''

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto!')
    elif tamanho_nome >=5 and tamanho_nome <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite mais de uma letra.')
 