
'''Transforma a ultima letra dos nomes que estão lista em maiusculo'''

nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [ 
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)