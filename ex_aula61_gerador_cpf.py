#74682489070
contador_regressivo = 10
resultado_digito_1 = 0



cpf_enviado = input('Informe os 9 PRIMEIROS digitos do seu cpf: ')
nove_digitos = cpf_enviado[:9] # fazendo o fatiamento


for digito in nove_digitos:
            
    resultado_digito_1 += int(digito) * contador_regressivo #Soma cada uma da multiplicações
    contador_regressivo -= 1 # faz a contagem regressiva
digito_1 = (resultado_digito_1 * 10) % 11 # Multiplica o resultado e pega o resto da divisão por 11
digito_1 = digito_1 if digito_1 <= 9 else 0 

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo2 = 11    

resultado2 = 0
for digito in dez_digitos:
    resultado2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1
digito_2 = (resultado2 * 10) % 11
digito_2 = digito_2 if digito_2 <=  9 else 0

cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_gerado_calculo:
    print(f'{cpf_enviado} é válido.')
else:
    print('CPF é inválido.')
