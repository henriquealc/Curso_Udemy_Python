'''
Calculo de IMC do Usuario
'''

nome = str(input('Informe seu nome: ')).strip()
altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso / (altura * altura)
print(f'{nome}, você pesa {peso}kg.\nSua altura é {altura}. \nSeu IMC é {imc:.2f}.')


