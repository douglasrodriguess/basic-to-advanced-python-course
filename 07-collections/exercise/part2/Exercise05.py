import numpy as np

mat = [[int(input(f'Adicione o numero [{i}][{j}]: ')) for i in range(2)] for j in range(2)]
num = int(input("Qual o numero voce quer pesquisar: "))

mat = [[print(f'Linha: {i}\nColuna: {j}') if mat[i][j] == num else '' for i in range(2)] for j in range(2)]
