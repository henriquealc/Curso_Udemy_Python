'''
Calculadora com while
'''

while True:
    
    print('{:^30}'.format('---------- CALCULADORA ----------'))
    
    num = int(input('Insira o valor: '))
    num2 = int(input('Insira o outro valor: '))
    print('='*35)
    calculo = input('Informe o operador que deseja (+,*,/,-): ')
    
    if num or num2 is None:
        print('Um ou mais números digitados são inválidos.')    
    elif calculo not in '+''-''/''*''-':
        print('Insira uma opção válida.')
    elif calculo == '+':
        resultado = num + num2
        print(resultado)
    
    elif calculo == '-':
        resultado = num - num2
        print(resultado)
    
    elif calculo == '*':
        resultado = num * num2
        print(resultado)
    
    elif calculo == '/':
        resultado == '/'
        print(resultado)
    
    sair = input('Deseja sair [s]im? ').lower().startswith('s')    
    if sair is True:
        break
print('Obtigado por usar nossa calculadora, até mais...')

