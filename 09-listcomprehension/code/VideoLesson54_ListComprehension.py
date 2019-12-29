"""
List Comprehension parte 2

- Adicionando estruturas lógicas as listas
"""

###################################################
print('Exemplo 1')
numeros = [1, 2, 3, 4, 5, 6]
print([numero for numero in numeros if numero % 2 == 0])
print([numero for numero in numeros if numero % 2 != 0])

# Qualquer numero por modulo de 2 é 0 e zero é False, not False = True
print([numero for numero in numeros if not numero % 2])
print([numero for numero in numeros if numero % 2])

print('Exemplo 2')
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)