import numpy as np

A = np.array([[1, 2], [3, 4]])

quant = A.size
lin, col = A.shape

vet = []
tabuleiro = [[vet.append(A[i][j]) if A[i][j] < 4 else f'' for i in range(lin)] for j in range(col)]
print(vet)