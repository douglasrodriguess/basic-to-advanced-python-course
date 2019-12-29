# Usando switch, escreve um programa que leia um numero inteiro de 1 a 7 e
#   imprima o dia da semana correspondente a este numero


while True:
    num = int(input('Digite um numero de 1 a 7: '))
    if num == 1:
        print('Segunda-feira')
        break
    if num == 2:
        print('Terca-feira')
        break
    if num == 3:
        print('Quarta-feira')
        break
    if num == 4:
        print('Quinta-feira')
        break
    if num == 5:
        print('Sexta-feira')
        break
    if num == 6:
        print('Sabado')
        break
    if num == 7:
        print('Domingo')
        break
