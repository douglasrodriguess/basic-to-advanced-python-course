# Faça um programa que imprima o Triangulo de Floyd

n = int(input('Digite a quantidade de linhas do Triangulo de Floyd: '))
print('-'*26)
print('Triangulo de Floyd: ')
number = 1
for line in range(1, n + 1):
    for elem in range(1, line + 1):
        print(number, end=" ")
        number += 1
    print()
print('-'*26)