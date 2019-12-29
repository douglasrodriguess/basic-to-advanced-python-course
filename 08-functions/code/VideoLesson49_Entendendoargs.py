"""
Entendendo *args

- O parâmetro *args em uma função, coloca os valores extras os valores extras informados como entrada em uma tupla.
- Lembre-se que as tuplas são imutáveis.

"""

####################################################################
# Exemplos do que não é legal


def soma_todos_numeros(num1 = 1, num2 = 1, num3 = 2):
    """
    Funcao que recebe tres parametros e retorna a soma desses tres numeros
    :param num1: numero 1
    :param num2: numero 2
    :param num3: numero 3
    :return: soma dos tres numeros
    """
    return num1+num2+num3


print(soma_todos_numeros(2, 3, 5))
print(soma_todos_numeros(5))

####################################################################
# Exemplo correto


def soma_de_todos_numeros_correto(nome, *args):
    return sum(args)


print(soma_de_todos_numeros_correto('Douglas'))
print(soma_de_todos_numeros_correto('Douglas', 1))
print(soma_de_todos_numeros_correto('Douglas', 3,3))

####################################################################
# Exemplo correto

def verificacao(*args):
    if 'Douglas' in args and 'Engenheiro' in args:
        return 'show'
    return 'nada'


print(verificacao())
print(verificacao('Douglas', 234.21, 'Engenheiro'))
print(verificacao('Engenheiro'))

####################################################################
# Exemplo correto

def soma_de_todos_numeros_correto_final(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_de_todos_numeros_correto(*numeros))

# O asterisco serve para que informemos ao Python que estamos passando como argumento
#   uma coleção de dados. Desta forma, ele saberá que precisará antes de desempacotar estes dados