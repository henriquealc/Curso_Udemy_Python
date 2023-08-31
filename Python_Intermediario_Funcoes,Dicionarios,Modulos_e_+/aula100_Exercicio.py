# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

# importa os dados da lista produtos que esta na pasta dados
from dados import produtos

print('LISTA DE PRODUTOS'.center(50))
print('=-' * 30)
print(*produtos, sep='\n')
print()

# Aumenta os preços dos produtos em 10% gerando uma nova lista
print('PRODUTOS COM 10% DE AUMENTO'.center(50))
print('=-' * 30)
novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] + (produto['preco'] * 0.10), 2) # round usado para colocar 2 casas decimais
    print(produto)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print()
print('PRODUTOS ORDENADOS PELO NOME DO MAIOR PARA O MENOR'.center(60))
print('=-' * 30)
produto_ordenados_por_nome = copy.deepcopy(produtos)
produto_ordenados_por_nome.sort(key=lambda value: value['nome'], reverse=True)
for produtonome in produto_ordenados_por_nome:
    print(produtonome)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print()
print('PRODUTOS ORDENADOS PELO PREÇO'.center(50))
print('=-' * 30)
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda value: value['preco'], reverse=False)
for produto in produtos_ordenados_por_preco:
    print(produto)
print()