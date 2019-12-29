"""
LISTAS ANINHADAS (Nested Lists)

"""
##############################################
print('EXEMPLO 1')
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)
print(type(listas))

##############################################
print('COMO ACESSAR')
print(listas[0])
print(listas[0][1])

##############################################
print('ITERANDO COM LOOP')
for lista in listas:
    for num in lista:
        print(num)

##############################################
print('ITERANDO COM LIST COMPREHENSION')
[[print(num) for num in lista] for lista in listas]

tabuleiro = [[num for num in range(1, 4)] for lista in range(1, 4)]
print(tabuleiro)

tabuleiro = [['X' if num % 2 == 0 else '0' for num in range(1, 4)] for lista in range(1, 4)]
print(tabuleiro)