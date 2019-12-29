def troque(**kwargs):
    auxA = int(kwargs['A'])
    auxB = int(kwargs['B'])
    B = auxA
    A = auxB
    return A, B

numbers = {'A': 2, 'B': 7}

print(troque(**numbers))