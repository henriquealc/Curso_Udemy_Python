salas = [ 
        #  0........1....
        ['Maria', 'Helena'],  # 0 
        
        # 0
        ['Elaine'],  # 1
        
        # 0........1.........2.....
        ['Luiz', 'João', 'Eduarda', ] #(0, 10, 20, 30, 40)]  # 2

]

# print(sala[0][1])
# print(sala[2][2])
# print(sala[2][3][2])

for sala in salas:
#     print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)