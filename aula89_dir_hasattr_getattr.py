# dir, hasattr e gerattr

# Verifica se a o metodo dentro da string
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo): # Verifica se a string tem o metodo 'upper'
    print('Existe UPPER')
    print(getattr(string, metodo)())
else:
    print('Não existe esse metodo', metodo)
