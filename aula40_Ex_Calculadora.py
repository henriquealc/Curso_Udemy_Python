'''
Calculadora com while
'''
resultado = 0

while True:
    num = int(input('Insira o valor: '))
    num2 = int(input('Insira o outro valor: '))
    calculo = input('Qual calculo deseja fazer? \nMultiplicação- (*) \nAdição- (+)...\n')
    sair = input('Deseja sair [s]im? ').lower().startswith('s')    
    
    if sair is True:
        break
    else:
        if calculo == '+':
            resultado = num + num2
        print(resultado)
        if calculo == '-':
            resultado1 = num - num2
        print(resultado1)


