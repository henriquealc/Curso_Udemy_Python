"""
exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade foram digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

'''MANEIRA FEITA POR MIM'''

# DA UM ERRO! 
# nome = str(input('Digite seu nome: '))
# idade = int(input('Digite a sua idade: '))

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espacos = nome.count(' ')  # conta quantos espaços contem no nome informado   

if nome and idade:  # Verifica se nome e idade foram digitados  
    print(f'Seu nome é: {nome}') 
    print(f'Seu nome invertido é: {nome[::-1]}')  # Inverte o nome recebido e o coloca de tras para frente
    
    if espacos == 0:  # Verifica se contem espaços no nome informado
        print('Seu nome não contém espaços.')
    else:
        print(f'Seu nome contém {espacos} espaços.')
    
    print(f'Seu nome contém {len(nome)} letras.')  # Verifica quantas letras a no nome informado
    print(f'A primeira letra do seu nome é: {nome[:1]}')  # Verifica a primeira letra do nome
    print(f'A última letra de seu nome é: {nome[-1:]}')  #  ''     ''    última letra do nome
else:
    print('Desculpe, você deixou campos vazios.')



'''MANEIRA FEITA PELO PROFESSOR'''

# nome  =  input ( 'Digite o seu nome: ' )
# idade  =  input ( 'Digite sua idade: ' )

# if nome  and  idade :
#     print ( f'Seu nome é { nome } ' )
#     print ( f'Seu nome invertido é { nome [:: - 1 ] } ' )

#     if  ' '  and  nome :
#         print ( 'Seu nome contém espaços' )
#     else:
#         print ( 'Seu nome NÃO contém espaços' )

#     print ( f'Seu nome tem { len ( nome ) } letras' )
#     print ( f'A primeira letra do seu nome é { nome [ 0 ] } ' )
#     print ( f'A última letra do seu nome é { nome [ - 1 ] } ' )
# else:
#     print ( "Desculpe, você deixou campos vazios." )