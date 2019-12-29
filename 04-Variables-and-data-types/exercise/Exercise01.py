# Faça um programa que leia um numero inteiro e imprima

aux = 0
while aux == 0:
    num = float(input("Digite um numero: "))
    if num == int(num):
        print(f'O numero {int(num)} eh inteiro.')
        aux = 1
    else:
        print(f'O numero {num} nao eh inteiro.')
