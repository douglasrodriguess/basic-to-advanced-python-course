"""
LIST COMPREHENSION

- Utilizando list comprehension, nós podemos gerar novas listas com dados processados a partir de outro iterável

- Sintaxe:
[ dado for dado in iteravel ]

"""
##################################################
print('EXEMPLO 1')
lista = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in lista]
print(res)

# Compreensão:
# 1- Para cada número na lista (for numero in lista)
# 2 - Número x 10

print('EXEMPLO 2')
res = [numero/2 for numero in lista]
print(res)

print('EXEMPLO 3')


def funcao (valor):
    return valor * valor


res = [funcao(numero) for numero in lista]
print(res)

print('EXEMPLO 4 - Loop')
numerodobrados = []
for numero in [1, 2, 3, 4, 5]:
    numerodobrados.append(numero*2)
print(numerodobrados)

print('EXEMPLO 5 - List Comprehension')
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

print('EXEMPLO 6')
nome = 'Douglas Rodrigues'
print([letra.upper() for letra in nome])

print('Exemplo 7')


def maisculo(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


nome = ['douglas', 'araujo', 'rodrigues']
print([maisculo(palavra) for palavra in nome])

print('Exemplo 8')
print([numero * 3 for numero in range(1, 10)])

print('Exemplo 9')
print([bool(valor) for valor in [0, [], True, '', 1, 2, 40]])

print('Exemplo 10')
print([str(numero) for numero in [1, 2, 3]])