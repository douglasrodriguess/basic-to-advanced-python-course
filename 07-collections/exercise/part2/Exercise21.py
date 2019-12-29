import numpy as np

A = np.array([[1, 2], [3, 4]])

quant = A.size
lin, col = A.shape

vet = []
tabuleiro = [[A[i][j] + 3 for i in range(lin)] for j in range(col)]
print(tabuleiro)