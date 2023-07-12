# Exemplo de uso dos sets 
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower()) # adiciona a letra dentro do set

    if 'l' in letras:
        print('PRABÉNS!')
        break
    print(letras)