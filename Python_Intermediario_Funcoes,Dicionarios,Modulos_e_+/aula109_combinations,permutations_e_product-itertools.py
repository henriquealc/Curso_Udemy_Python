# Combinations, Permutationse e Product - itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


'''O que esse def faz'''

# Sem o list so aparecera o numero de onde esta guardado na memoria
# * - Espande a lista
# sep='\n' - Usado para quebrar a linha
def printinter (iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = ['João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'], 
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]


# Imprimi a lista pessoas em grupos de 2
printinter(combinations(pessoas, 2))

# Pode ter repetições 
printinter(permutations(pessoas, 2))

# * - Desempacota
printinter(product(*camisetas))