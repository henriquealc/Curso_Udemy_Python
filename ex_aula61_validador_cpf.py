import sys
import re # importa a biblioteca 're' e usa o metódo 'sub' para remover algumas coisas digitadas pelo usuario

#74682489070
contador_regressivo = 10
resultado_digito_1 = 0


while True:
    cpf_entrada = input('Informe o CPF para saber se é válido: ')  #.replace('.', '').replace('-', '').replace(' ','') # Substitui os espaços, ponto e virgula.
    
    # So pega os números e remove tudo aquilo que não é número
    cpf_enviado = re.sub(
        r'[^0-9]' # Substitui tudo que é número de 0 a 9
        , '', 
        cpf_entrada
    )
     
    # Feito para evitar que o usuario digite numeros ou letras sequencias Ex: 11111111 ou aaaaaaa   
    entrada_e_sequencial = cpf_entrada == cpf_entrada[0] * len(cpf_entrada)

    if entrada_e_sequencial:
        print('Você enviou dados sequenciais.')
        sys.exit() # Mata o codigo, para o programa
    
    nove_digitos = cpf_enviado[:9] # fazendo o fatiamento
    
    # OBS: NÃO ENTRA NESSE IF
    # if len(cpf_enviado) == 9: 
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
# else:
#         print('INFORME APENAS NÚMEROS!')