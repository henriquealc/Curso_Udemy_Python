texto = 'amor'
tentativas = 0
letras_acertadas = ''

while True:
    letra = input('Digite uma letra: ')
    # tentativas += 1
    
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    
    if letra in texto:
        letras_acertadas += letra
    
    for letra_secreta in texto:
        if letra_secreta in letras_acertadas:
            print(letra_secreta) 
    else:
        print('*')
print(f'Você efetuou {tentativas} tentativas!')

