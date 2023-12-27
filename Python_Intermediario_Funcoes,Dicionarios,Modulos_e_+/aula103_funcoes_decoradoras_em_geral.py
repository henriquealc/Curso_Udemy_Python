'''
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
Usar as funções decoradoras em outras funções.
'''
def inverte_string(string):
    try:
        string = string[::-1]
        return string
    except(TypeError):
        print('Informe apenas strings!')
        return ''

str = inverte_string("Casa Amarela")
print(str)