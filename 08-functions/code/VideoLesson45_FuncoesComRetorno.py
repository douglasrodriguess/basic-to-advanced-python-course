"""
FUNCOES COM RETORNO

"""

##############################################################
# EXEMPLOS
print()
print('-'*30)
print('EXEMPLOS DE FUNCOES')
print()


# Exemplo 1

numeros = [1, 2, 3]
ret = numeros.pop()
print(ret)
print(numeros)

##############################################################
# EXEMPLOS
print()
print('-'*30)
print('TRABALHANDO COM O RETORNO DAS FUNCOES')
print()

# Exemplo 2

# Essa funcao nao retorna nada
def quadrado_de_7():
    print(7*7)
ret = quadrado_de_7()
# Quando tentamos retornar algo de uma funcao sem retorno, ela retorna o None
print(ret)

# Essa funcao com retorno
def quadrado_de_7():
    return 7*7
# Criamos uma variavel pra receber o retorno de uma funcao
# Nao necessariamente temos que criar uma variável pra receber o retorno de uma funcao
ret = quadrado_de_7()
print(ret)

# A funcao return finaliza a funcao, pode ter varios returns na funcao...
#           No entanto, apenas haverá o retorno só de um um return.

# Exemplo 3

# Podemos retornar varios tipos de variáveis no return, inclusive múltiplos valores

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(outra_funcao())
print(type(outra_funcao()))

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    print(valor)
    if valor > 0.5:
        return "Cara"
    return "Coroa"

print(joga_moeda())