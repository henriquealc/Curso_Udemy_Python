# Try, except, else e finally

a = 18
b = 2
c = a / b

try:
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError: # Quando tentar dividir um dos valores por 0
    print('Dividiu por zero.')
except NameError: # Quando uma das variaveis não estiver definida
    print('Nome b não está definido')
except (TypeError, IndexError) as error: # as error: Cria uma estensão dos tipos de erro, error vira como se fosse uma variavel
    print('TypeError + IndexError')
    print('Nome:', error.__class__.__name__) # Mostra o nome do error
except Exception: # Qualquer outro erro que não esteja a cima 
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')