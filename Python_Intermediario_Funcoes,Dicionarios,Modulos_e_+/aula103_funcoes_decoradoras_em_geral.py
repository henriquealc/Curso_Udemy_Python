'''
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
Usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar" (Açúcar sintático)
'''

'''Ex feito por mim'''
# def inverte_string(string):
#     try:
#         string = string[::-1]
#         return string
#     except(TypeError):
#         print('Informe apenas strings!')
#         return ''

# str = inverte_string('Casa Amarela')
# print(str)



'''Exeplo feito pelo professor'''

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao # decoradores
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    

# inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('123')
print(invertida)