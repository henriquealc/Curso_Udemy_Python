# Count é um iterador sem fim
# Count contador infinito
# Count não esta no python tem que importar
# Não pode chamar o __next__ no range

'''Comparando o count com o range'''


from itertools import count

#count(inicio, multiplo)
#count pode passar argumentos nomeados start = começa/ step= pula de 8 em 8
c1 = count(step= 8, start=0) # Só se pode passar o inicio e multiplos

#range(inicio, fim, multiplo)
r1 = range(10, 100, 8) # Range eu sempre tenho que passar aqui um argumento onde quero que termine


print('c1', hasattr(c1, '__iter__')) # Verifica se é um iteravel
print('c1', hasattr(c1, '__next__')) # Verifica se pode usar o next
print('r1', hasattr(r1, '__iter__')) # verifica se é um iteravel
print('r1', hasattr(r1, '__next__')) # O next não funciona no range

print()
print('count')
for i in c1:
    if i > 100: # Sem o if cria um loop infinito e passo até onde quero que o count vá
        break
    print(i)

print()

# Exemplo de como o range funciona em comparação ao count
print('Range')
for i in r1:
    print(i)


