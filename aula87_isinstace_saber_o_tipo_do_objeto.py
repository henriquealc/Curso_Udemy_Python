# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a' , 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'}, 'b',
]

for item in lista:
    if isinstance(item, set):  # Mostra quais são os tipos dos items que estão dentro da lista
        print('SET')
        item.add(5) # Adiciona o número 5 dentro do elemento do tipo set
        print(item, isinstance(item, set))
    
    elif isinstance(item, str): # Verifica quais são os items do tipo string
        print('STR') 
        print(item.upper()) # Coloca os items que são str em maiunsculo
    
    elif isinstance(item, (int, float)): # Verifica quais são os items inteiros ou float
        print('NUM')
        print(item, item * 2) # Mostra os items inteiros e float e multiplica cada um deles por 2
    
    else:
        print('OUTRO') # Caso os items não se encaixe nos tipo verificado acima
        print(item)