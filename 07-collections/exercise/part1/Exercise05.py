vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

contpar = 0
contimpar = 0
for num in vetor:
    if num % 2 == 0:
        contpar+=1
    else:
        contimpar+=1
        
print(contpar)
print(contimpar)

