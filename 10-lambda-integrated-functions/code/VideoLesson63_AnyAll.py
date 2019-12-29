"""
ANY e ALL

all() -> retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
any() -> retorna True se qualquer um dos elementos do iterável são verdadeiros

"""
print('#################################################################')
print('Exemplo de all()')
print(all([0, 1, 2, 3, 4, 5]))  # É falso por conta que o 0 é False
print(all([1, 2, 3, 4, 5]))
print(all([]))

nomes = ['Douglas', 'Davi', 'Diego']
print(all([nome[0] == 'D' for nome in nomes]))
nomes = ['Douglas', 'Davi', 'Diego', 'Rafael']
print(all([nome[0] == 'D' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))

print('#################################################################')
print('Exemplo de any()')
nomes = ['Douglas', 'Davi', 'Diego', 'Rafael']
print(any([nome[0] == 'R' for nome in nomes]))
nomes = ['Douglas', 'Davi', 'Diego', 'Rafael']
print(any([nome[0] == 'V' for nome in nomes]))

