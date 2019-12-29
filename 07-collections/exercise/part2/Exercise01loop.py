import numpy as np

A = np.array([[1, 2], [3, 4]])

quant = A.size
lin, col = A.shape

for i in range(lin):
    for j in range(col):
        if A[i][j] < 2:
            print(A[i][j])

