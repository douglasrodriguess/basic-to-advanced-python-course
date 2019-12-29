# Programa que faz varias operações basicas
import statistics


vet = []
while True:
    num = float(input('Digite um numero: '))
    vet.append(num)
    escolha = input('Quer digitar outro numero: ')
    if escolha == 'nao':
        break
print('-'*39)
print(f'A soma dos numeros digitado eh {sum(vet)}')
print(f'A quantidade de numeros digitados eh {len(vet)}')
if len(vet) > 1:
    print(f'A media dos numeros digitados eh {statistics.mean(vet)}')
else:
    print(f'A media dos numeros digitados eh {vet[0]}')
print(f'O maior numero digitado eh {max(vet)}')
print(f'O menor numero digitado eh {min(vet)}')

vetpar = []
for pos in range(0, len(vet)):
    number = vet[pos]
    if number % 2 == 0:
        vetpar.append(number)
if len(vet) > 1:
    print(f'A media dos numeros pares eh {statistics.mean(vetpar)}')
else:
    print(f'A media dos numeros pares eh {vetpar[0]}')

