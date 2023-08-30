# Formas diferentes de importar os package
# Apenas o import packtage NÃO FAZ NADA

from aula99_package.modulo import soma_valores
print(soma_valores(1, 2))

import aula99_package.modulo
print(aula99_package.modulo.soma_valores(1,2))

from aula99_package import modulo
print(modulo.soma_valores(2, 1))

# Considerado má prática de programação
# '*' se chama all
from aula99_package.modulo import *
print(soma_valores(1, 2))



# Usando o all
print(variavel)
print(nova_variavel)

# import aula99_package.modulo
# print(soma_valores(2, 5))