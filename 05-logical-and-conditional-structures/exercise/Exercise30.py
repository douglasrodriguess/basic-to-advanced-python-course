# Faça um programa que receba três números e mostre-os em ordem crescente

vet = []
num = 0
for num in range(3):
    vet.append(float(input(f'Digite o seu numero {num}: ')))
vet.sort()
print(f'Os numeros em ordem crescente eh: {vet}')