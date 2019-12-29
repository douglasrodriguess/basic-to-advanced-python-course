"""
Set Comprehension

"""
################################
print('Exemplo 1')
numeros = {num for num in range(1, 7)}
print(numeros)

print('Exemplo 2')
numeros = {X ** 2 for X in range(10)}
print(numeros)

print('Exemplo 3')
numeros = {X: X ** 2 for X in range(10)}
print(numeros)
print(type(numeros))

print('Exemplo 4')
letras = {letra for letra in 'Douglas Araujo'}
print(letras)