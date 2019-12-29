# Leia a opção do usuário e execute a operação escolhida
# Escreve uma mensagem de erro se a opção for inválida

import numpy

def solicitacao(vet, opcao):
    if opcao == 4:
        vet[0] = float(input('Digite o numerador: '))
        while vet[1] == 0:
            vet[1] = float(input('Digite o denominador: '))
    else:
        vet[0] = float(input('Digite o primeiro numero: '))
        vet[1] = float(input('Digite o segundo numero: '))
    return vet


vet = [0, 0]
opcao = 10
print(type(opcao))
while 0 > opcao or opcao > 5:
    print('Escolha a opcao: ')
    print('1- Soma de 2 numeros')
    print('2- Diferenca entre 2 numeros (maior pelo menor)')
    print('3- Produto entre dois 2 numeros')
    print('4- Divisao entre 2 numeros (o denominar nao pode ser zero)')
    opcao = int(input('Digite a sua opcao: '))

if opcao == 1:
    solicitacao(vet, opcao)
    res = sum(vet)
elif opcao == 2:
    solicitacao(vet, opcao)
    vet.sort()
    res = vet[1] - vet[0]
elif opcao == 3:
    solicitacao(vet, opcao)
    vet.sort()
    res = numpy.prod(vet)
else:
    solicitacao(vet, opcao)
    res = vet[0] / vet[1]

print(f'O resultado da opcao {opcao} eh {res}')