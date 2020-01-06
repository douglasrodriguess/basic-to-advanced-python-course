"""
Tipo numérico

"""

print('-'*40)
print("Numero inteiro")
print(f'{int(5/2)}')
print(f'{5//2}')

print('-'*40)
print("Numero par (resultado do % eh 0) ou ímpar (resultado do % eh 1)")
print(f'{7 % 2}')
print(f'{8 % 2}')

print('-'*40)
print("Potencia")
print(f'{2 ** 8}')

print('-'*40)
print("Variável auxíliar")
num = 10
num += 2
print(f'{num}')
num = 10
num -= 2
print(f'{num}')
num = 10
num *= 2
print(f'{num}')
num = 10
num /= 2
print(f'{num}')

print('-'*40)
# A Função type() retorna o tipo numérico daquela variável
print("Funcao type()")
num = 4
print(type(4))
num = 4.3
print(type(num))

# Separação de um valor muito grande
#     1_000_000_000
