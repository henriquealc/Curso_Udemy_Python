# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else: # Será executado caso não ocorra nenhum erro
    print('Não deu erro')
finally: # Finally sempre é executado
    print('FECHAR ARQUIVO')