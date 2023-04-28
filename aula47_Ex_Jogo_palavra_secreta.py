import os
texto = 'sabedoria'
tentativas = 0
letras_acertadas = ''

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    #  Verifica quantas letras o usuario digitou
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    
    # Verifica se a letra esta na variavel texto
    if letra in texto:
        letras_acertadas += letra
    
    palavra_formada = ''
    # Percorre cada letra da variavel texto
    for letra_secreta in texto:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta 
        else:
            palavra_formada += '*'      
    
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == texto:
        os.system('clear')
        print('VOCÊ GANHOU!!! PARABÉNS!!')
        print(f'A palavra era {texto}')
        print(f'Você efetuou {tentativas} tentativas!')
        letras_acertadas = ''
        tentativas = 0        
