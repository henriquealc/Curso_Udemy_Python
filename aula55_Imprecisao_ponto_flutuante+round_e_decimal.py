# Usar a biblioteca decimal apenas se o número de ponto flutuante for muito grande e precisa do ultimo número
import decimal
numero_1 = decimal.Decimal('0.1') 
numero_2 = decimal.Decimal('0.7')
soma_num = numero_1 + numero_2

print(soma_num)
print(f'{soma_num}:.2f') # o mais indicado pra usar no dia a dia 
print (round(soma_num, 3)) # arredonda a casa decimal final