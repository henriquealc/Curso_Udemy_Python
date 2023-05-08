"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

'''RESOLUÇÃO FEITA POR MIM'''
import os
lista = [] # Sempre criar a variavel lista fora da estrutura de repetição


while True:
    opcao = input('Selecione uma opção: \n[i]nserir [a]apagar [l]istar s[air]: ').lower()
    if opcao == 'i':
        os.system('cls')
        inserir = input('Valor: ')
        lista.append(inserir)
    elif opcao == 'a':
        os.system('cls')
        apagar = input('Digite o indice que deseja apagar: ')
        
        try:
            indice = int(apagar)
            del lista[indice] # deletar um indice da lista
        
         # informa o erro
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        print(lista) # Informa a lista e os itens que contém nela
        
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
        # mostra os indices da lista
    elif opcao == 's':
        print('Programa encerrado com sucesso, Obrigado!')
        break
    else:
        print('Por favor escolha i, a ou l.')




# Resolução feita pelo professor

'''import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')'''