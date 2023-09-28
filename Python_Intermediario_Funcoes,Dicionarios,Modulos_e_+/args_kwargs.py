def calcular_imposto(valor):
    ir = valor * 0.275
    iss = valor * 0.03
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print(calcular_imposto(100))
print(calcular_imposto(valor=1000)) # outra forma



# Argumentos de posição
def calcular_imposto(valor, perc_ir):
    ir = valor * perc_ir
    iss = valor * 0.03
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print(calcular_imposto(1000, 0.25))
print(calcular_imposto(valor=1000, perc_ir=0.25))
print(calcular_imposto(1000, perc_ir=0.25)) # Se inverter vai dar erro




# Args pode passar quantos argumentos de posição quiser
# Args é uma tupla, pode percorrer cada item dentro dela
def calcular_imposto(valor, *args):
    total_imposto = 0
    print(args)
    for item in args:
        total_imposto += valor * item
    return total_imposto

print(calcular_imposto(1000, 0.275, 0.05, 0.0375, 0.03))



# Kwargs permite passar varios parametros, sempre dando nome para eles
# kwargs é um dicionario
# Kwargs pode criar condições
def calcular_imposto_trimestral(valor, **kwargs):
    total_imposto = 0
    print(kwargs)
    if 'perc_ir' in kwargs:
        total_imposto += valor * kwargs['perc_ir']
    if 'per_csll' in kwargs:
        total_imposto += valor * kwargs['perc_csll']
    return total_imposto

print(calcular_imposto_trimestral(1000, perc_ir=0.275, perc_iss=0.05, perc_csll=0.0375, perc_is=0.03))

