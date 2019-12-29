vet = [0, 1, 2, 3, 4, 5, 6, 7]

print(5 in vet)
print(100 in vet)

soma = 0
for ind in vet:
    if vet[ind] == 5 or vet[ind] == 6:
        soma += vet[ind]

print(f'A soma eh {soma}')
