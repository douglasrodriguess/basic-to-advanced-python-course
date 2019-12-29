"""
DICTIONARY COMPREHENSION

Sintaxe:
{chave: valor for valor in iteravel}
"""
####################################
print('EXEMPLO 1')
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

print('EXEMPLO 2')
numeros = {1, 2, 3, 4, 5}
quadrado = {valor: valor ** 2 for valor in numeros}

print('EXEMPLO 3')
chave = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chave[i]: valores[i] for i in range(0, len(chave))}
print(mistura)

print('EXEMPLO 4')
numeros = {1, 2, 3, 4, 5}
res = {num:{'par' if num % 2 == 0 else 'impar'} for num in numeros}
print(res)