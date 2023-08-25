'''
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
'''

# condicao = 10 == 11
# variavel = 'valor' if condicao else 'Outro Valor'
# print(variavel)

digito = 9 # > 9 = 0
''' se digito for maior que 9 imprimi 0, se digito for menor imprimi o digito'''
# novo_digito = digito if digito <= 9 else 0 


'''imprime 0 se digito for maior que 9, se for menor imprimi o digito informado'''
novo_digito = 0 if digito > 9 else digito
print(novo_digito)