vetor = [-100, 1, 0, 3, 8, 98, 6, -7, 8, 9]

print(0 in vetor)
vet = vetor.copy()
for ind, valor in enumerate(vet):
    if valor == 8:
        print(ind)
        aux = vetor.copy()
        aux.remove(valor)
        vetor = aux.copy()

print(vetor)

