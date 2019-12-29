"""
FUNCOES COM PARAMETROS

- Funcoes que recebem dados para serem trabalhados dentro da funcao
- Entrada -> processamento -> saída

"""

##############################################################

# Refatorando uma funcao 1

def quadrado(numero):
    return numero ** 2

print(quadrado(7))

# Refatorando uma funcao 2

def cantar_parabens(aniversariantes):
    print("Hora de cantar parabens")
    print("Parabens!")
    print(aniversariantes)

cantar_parabens('Marcos')

# Multiplas entradas

def soma (a, b, msg):
    return a * b * msg

operacao = soma(2, 3, 'Douglas')
print(operacao)

##############################################################
# NOMEANDO PARÂMETROS
print()
print('-'*30)
print('NOMEANDO PARÂMETROS')
print()

# O que tá aqui são parâmetos
def nome_completo(nome, sobrenome):
    return nome + sobrenome

# O que tá aqui são argumentos
print(nome_completo('Douglas', 'Rodrigues'))

##############################################################
# ARGUMENTOS NOMEADOS
print()
print('-'*30)
print('ARGUMENTOS NOMEADOS')
print()

# Caso utilizarmos os nomes dos parâmetros nos argumentos para
#       informá-los, podemos utulizar quaisquer ordem

def nome_completo(nome, sobrenome, space):
    return nome + space + sobrenome

print(nome_completo(sobrenome = 'Rodrigues', nome = 'Douglas', space= ' '))

