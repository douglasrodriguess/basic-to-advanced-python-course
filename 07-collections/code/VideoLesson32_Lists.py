"""
Listas
Listas em Python funciona como vetores/matrizes(arrays) em outras linguagens,
com a diferença de serem DINÂMICOS e também de podermos colocar QUALQUER tipo
de dado.
DINÂMICO: não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente
ir adicionando elementos;
QUALQUER tipo de dados: não possuem tipo de dado fixo, ou seja, podemos colocar
qualquer tipo de dados;
As listas são representadas por colchetes []
As listas são mutáveis, ou seja, elas podem mudar constantemente
"""

type([])

lista1 = [1, 3, 3, 9, 10, 23, 24]
lista2 = ['D', 'O', 'U', 'G', 'L', 'A', 'S']
lista3 = []
lista4 = list(range(11))
lista5 = list('Douglas Rodrigues')
nome1 = 'Douglas De Araujo Rodrigues'
nome2 = 'Douglas, Helena'
lista7 = ['Douglas', 'de', 'Araujo', 'Rodrigues']
cores = ['verde', 'amarelo', 'azul', 'branco']
lista8 = [1, 2, 4]
# Checar se determinado valor está contido na lista
"""
num = 3
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print("Não encontrei o {num}.")

# Adicionar no final da lista
lista1.append(65)
print(lista1)

# Adicionar mais de um termo no final da lista
lista1.extend([76, 865])
print(lista1)

# Adicionar um termo em uma posição da lista
lista1.insert(2, 32)
print(lista1)

# Somar duas listas
somalista = lista1 + lista2
print(somalista)

# Inverter a ordem de uma lista
lista1.reverse()
print(lista1)

# Inverter a ordem de uma lista
print(lista1[::-1])

# Organizar em ordem crescente
lista1.sort()
print(lista1)

print()

# Converter uma string para lista
#    Forma padrão
print(nome1)
lista6 = nome1.split()
print(lista6)
#    Forma com virgula
print(nome2)
lista6 = nome2.split(',')
print(lista6)

print()

# Converter uma lista em uma string
#     Separando por espaço
nome3 = ' '.join(lista7)
print(nome3)
#     Separando com outra coisa
nome3 = '$'.join(lista7)
print(nome3)

# Para entender o índice negativo, pense como um circulo, onde o final
#     de um elemento está ligado com o final da lista
print(cores)
print(cores[-1])
# print(cores[-5]) Erro pois não existe indice -5.
#    Exemplo com for
for cor in cores:
    print(cor)
print()
#    Exemplo com while
ind = 0
while ind < len(cores):
    print(cores[ind])
    ind += 1
    
# Gerar indice com for
for indice, cor in enumerate(cores):
    print(indice, cor)
    
# Encontrar o índice de um elemento em uma lista
numeros = [5, 4, 6, 6, 10, 8, 6]
print(numeros.index(4))
#    Caso de duplicidade, ele retorna o índice do primeiro valor encontrado
print(numeros.index(6))
#    Caso não tenha esse elemento na lista, será apresentado erro ValueError
# print(numeros.index(1))
#    Buscando dentro de um range, ou seja, definindo o índice para começar a buscar
print(numeros.index(6,5))
#    Buscando dentro de um range, ou seja, definindo um intervalo
print(numeros.index(8, 3, 6))
    
# Revisão de slice
# lista(inicio: fim: passo)
# range(inicio: fim: passo)

print(lista1[1])
print(lista1[::])
print(lista1[1:])  # Começa no indice 1
print(lista1[:3])  # Começa em zero e vai até o passo 2
print(lista1[::2])  # Trabalhando com o passo
print(lista1[::-1])    

# Tranformar uma lista em tupla
tupla = tuple(lista1)
print(lista1)  # Separado por []
print(tupla)  # Separado por ()

# Desampacotamento de listas
#    Se tivermos um numero diferente de elementos e variaveis
#        vai dar ValueError
num1, num2, num3 = lista8

# Copiando uma lista para outra
#    Copy (Deep Copy)
nova = lista8.copy()
print(lista8)
print(nova)
nova.append(3)
print(lista8)
print(nova)
#    Shallow: após realizar uma modificação, ambas as listas foram modificadas
nova = lista8
print(lista8)
print(nova)
nova.append(3)
print(lista8)
print(nova)
"""

