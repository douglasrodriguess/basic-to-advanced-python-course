
A = [1, 0, 5, -2, -5, 7]

print(f'O tipo do vetor eh {type(A)}')
print(f'O tamanho do vetor sendo conjunto eh {len(set(A))}')

soma = A[0] + A[1] + A[5]
print(f'O tipo do vetor eh {type(A)}')
print(f'A soma eh {soma}')

A.insert(4, 100)
print(f'O vetor eh {A}')

print('Os elementos do vetor em cada linha eh:')
for ind in A:
    print(ind)
