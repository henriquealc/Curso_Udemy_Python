# groupby - agrupando valores (itertools)

alunos = [{'nome': 'Luiz', 'nota': 'A'},
          {'nome': 'Letícia', 'nota': 'B'},
          {'nome': 'Fabricio', 'nota': 'A'},
          {'nome': 'Rosemary', 'nota': 'C'},
          {'nome': 'Joana', 'nota': 'D'},
          {'nome': 'João', 'nota': 'A'},
          {'nome': 'Eduardo', 'nota': 'B'},
          {'nome':'André', 'nota': 'A'},
          {'nome':'Anderson', 'nota': 'C'},
]

for nome in alunos:
    print('O aluno', nome['nome'], 'teve a nota', nome['nota'])
    