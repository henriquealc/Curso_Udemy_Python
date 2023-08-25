''' For aninhado '''
# for x in range(10):
#     for y in range(5):
#         print(x, y)



'''Fazendo linhas e colunas com list comprehension'''
# Na list comprehesion um for fica dentro do outro

linhas_e_colunas =[
    (x, y)
    if y != 2 else (x, y * 1000) # Se y for 2 multiplica ele por 1000
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2 # Se x for 2 não aparece
]

print(linhas_e_colunas)