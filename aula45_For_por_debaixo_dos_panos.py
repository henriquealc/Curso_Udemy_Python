'''
Iterador -> quem sabe entrega um valor por vez
next -> me entregue o próximo valor 
iter -> me entregue seu iterador
'''

# for letra in texto
# Como o for funciona por debaixo dos panos
texto = 'Luiz' #iterável

iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopAsyncIteration:
        break

# for resumido
for letra in texto:
    print(letra)