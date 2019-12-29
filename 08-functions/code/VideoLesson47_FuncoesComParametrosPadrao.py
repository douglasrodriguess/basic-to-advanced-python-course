"""
FUNÇÕES COM PARAMETROS PADRÃO (DEFAULT PARAMETERS)

# Funções em que a presença do parâmetro é opcional

"""

##############################################################
# EXEMPLOS

# Exemplo 1
print('Douglas')
print()

# Exemplo 2
# Se eu já informar um valor padrão, não vai dar erro
#    Se eu informar um valor durante o momento que chamo a função, esse novo
#             valor irá  substituir o valor padrão da função
def exponencial(numero = 4, potencia=2):
    return numero ** potencia


print(exponencial(3, 8))
print(exponencial())

# Obs: os parâmetros default devem sempre estar ao final da declaração

# Exemplo 3

def mostra_informacao (nome='Douglas', instrutor=False):
    if nome == 'Douglas' and instrutor:
        return 'Bem-vindo instrutor Douglas'
    elif nome == 'Douglas':
        return 'Eu pensei que voce fosse o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Roberto'))
print(mostra_informacao(nome='Itrio'))

# Exemplo 4


def soma (num1, num2):
    return num1+num2

def subtracao (num1, num2):
    return num1-num2

def mat (num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(2, 3))
print(mat(2, 3, subtracao))


# Exemplo 5

# Evite variáveis globais
# UnboundLocalError (A variável local não foi inicializada

total = 0


def incremento():
    global total # Avisando que é pra ser usado a variável global total na função, pois o algoritmo dá preferência pra função local
    total = total + 1
    return total


print(incremento())

# Exemplo 6


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())

