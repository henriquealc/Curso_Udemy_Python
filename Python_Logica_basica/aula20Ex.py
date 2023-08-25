num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print(f'O primeiro valor= {num1} é maior que o segundo valor= {num2}.')
elif num1 < num2:
    print(f'O segundo valor= {num2} é maior que o primeiro valor= {num1}.')
else:
    print(f'O primeiro valor= {num1} contém o mesmo valor que o segundo= {num2}.')
print('Programa encerrado.')