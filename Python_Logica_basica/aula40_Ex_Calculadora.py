'''
Calculadora com while
'''

while True:
    
    print('{:^30}'.format('---------- CALCULADORA ----------'))
    
    num = input('Insira o valor: ')
    num2 = input('Insira o outro valor: ')
    print('='*35)
    calculo = input('Informe o operador que deseja (+,*,/,-): ')
    
    
    numeros_validos = None  # numeros validos recebe sem valor

    try:  
        num_1_float = float(num)  # transforma os números em float
        num_2_float = float(num2) #     ' '         ''        '' 
        numeros_validos = True  
    except:
        numeros_validos = None
    
    if numeros_validos is None:  # Verifica se None é True
        print('Um dos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if calculo not in operadores_permitidos:  # Verifica se o usúario inserio operador válido
        print('Operador inválido.')
        continue
    
    elif len(calculo) > 1:  # Verifica se o usúario digitou mais de um operador 
        print('Digite apenas um operador.')
        continue
    
    # Verifica qual das opções de operação o usúario digitou
    elif calculo == '+':
        resultado = num + num2
        print(f'O resultado na adição é: {resultado}')
    
    elif calculo == '-':
        resultado = num - num2
        print('O resultado da subtração é: {resultado}')
    
    elif calculo == '*':
        resultado = num * num2
        print('O resultado da multiplicação é: {resultado}')
    
    elif calculo == '/':
        resultado == '/'
        print('O resultado da divisão é: {resultado}')
    
    # Caso o usúario digite 's' para encerrar o programa
    sair = input('Deseja sair [s]im? ').lower().startswith('s')    
    if sair is True:
        break
print('Obtigado por usar nossa calculadora, até mais...')

