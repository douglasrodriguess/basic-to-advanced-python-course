"""
Loop for

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteraveis:
- String
    nome = "Geek university"
- Lista
    lista = [1, 2, 3, 5, 10]
- Range
    numeros = range(1, 10)

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

Python:

for item in iteravel:
    execucao  do loop

"""

import emoji

# Iteráveis
nome = "Douglas Rodrigues"
lista = [1, 2, 3, 5, 10]
numeros = range(1, 10)

print("Exemplo de for (iterando sobre uma string)")

print("Para cada letra dentro desse iteravel, faça isso:")
for letra in nome:
    print(letra)

print("O enumerate retorna o índice e o valor")
for indice, letra in enumerate(nome):
    print(nome[indice])

for ind_let in enumerate(nome):
    print(ind_let)

print("O enumerate retorna o valor do índice")
for valor in enumerate(nome):
    print(valor[0])

print("O enumerate retorna o valor do valor")
for valor in enumerate(nome):
    print(valor[1])

print("Quando não precisamos do indice, descartamos com um '_'")
for _, letra in enumerate(nome):
    print(letra)

print("-"*40)
print("Exemplo de for (iterando sobre uma lista)")

for numero in lista:
    print(numero)

print("-"*40)
print("Exemplo de for (iterando sobre um range)")

""" 
    range(valor_inicial, valor_final)
    o valor final não é inclusive
"""

for numero in range(1, 10):
    print(numero)

# Usando o Python 3.x
qtd = int(input('Quantas vezes esse loop deve ser executado? '))
soma = 0

for aux in range(1, qtd+1):
    num = int(input(f'Informe o {aux}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Douglas Rodrigues'
for letra in nome:
    print(letra, end='')

print()
print("-"*40)
print("Imprimindo Emoticons")

# site: https://apps.timwhitlock.info/emoji/tables/unicode
# original = U+1F60D
# modificado = U0001F60D
print()
for num in range(1, 10):
    print('\U0001F60D' * num)

