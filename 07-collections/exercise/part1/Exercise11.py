import numpy as np

vetor = [0, 1, -2, 3, 4, 5, 6, -7, 8, 9]

cont = 0
soma = 0
for num in vetor:
    if num<0:
        cont += 1
    else:
        soma += num

print(cont)
print(soma)
