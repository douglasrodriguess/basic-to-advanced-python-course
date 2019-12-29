# Peça ao usuário para digitar três valores inteiros e imprima a soma deles

vet = []
num = 0
lim = 3
for num in range(3):
    value = int(input(f'Digite o numero {num+1} da sua lista: '))
    vet.append(value)
soma=sum(vet)
print(f'A soma dos numeros {vet} eh {soma}')