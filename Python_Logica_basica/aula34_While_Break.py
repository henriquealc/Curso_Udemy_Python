"""
Repetições
enquanto (enquanto)
Executar uma ação enquanto uma condição para verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é: {nome}')
    
    if nome == 'sair':
        break
print('Acabou')
