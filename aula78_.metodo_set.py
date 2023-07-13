# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = {1, 2, 3, 3, 3, 3, 3, 3, 1} # Elimina os valores duplicados e so retorna 1 deles
# print(s1)

'''Remove os valores repetidos, os sets não garantem a ordem'''
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)

# formas de verificar se tem o valor dentro do set
# s1 = {1, 2, 3}
# print(3 not in s1)

# for numero in s1:
#     print(numero)




# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz') # adiciona o valor no set
s1.add(1) # so pode adicionar um valor por vez
#s1.update('Olá mundo') # adiciona o valor mas as letras NÃO ficam em ordem
s1.update(('Olá mundo', 1, 2, 3, 4)) #adiciona os valores sem bagunça as letras
# s1.clear() # limpa todo o set
s1.discard('Olá mundo') # descarta o valor passado, so pode passar 1 argumento por vez
# print(s1)



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # Une os sets, mas não repeti os valores iguais
s3 = s1 & s2  # Retor os itens presentes em ambos os sets
s3 = s2 - s1  # Retorna os itens presentes apenas no set da esquerda (a ordem importa)
s3 = s1 ^ s2  # Retorna os itens que não esta presente em ambos 
print(s3)