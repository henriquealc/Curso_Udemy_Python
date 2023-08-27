# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula97_m
from aula97_m import soma, variavel_modulo


# print('Este módulo se chama', __name__)
# Os prints da variavel modulo faz as mesmas coisas
print(variavel_modulo)
print(aula97_m.variavel_modulo)

# Os prints da soma tem a mesma funcionalidade
print(soma(2, 5))
print(aula97_m.soma(3, 2))