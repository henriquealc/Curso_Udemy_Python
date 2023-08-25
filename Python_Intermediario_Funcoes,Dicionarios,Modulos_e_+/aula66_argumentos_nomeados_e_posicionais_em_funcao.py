"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma (x, y, z):
    total = x + y + z
    print(f'{x=} y={y} {z=} = {total}', '|', 'x + y + z = ', x + y + z)

soma (1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')