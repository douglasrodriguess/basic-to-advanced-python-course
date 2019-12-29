# Faça um programa que calcule a diferença do quadrado da soma dos dez primeiros
#    numeros naturais com a soma dos quadrados dos dez primeiros numeros naturais

case1 = 0
case2 = 0
for num in range (1,101,1):
    case1 += num**2
    case2 += num
diferenca = case2**2 - case1
print(f'A diferenca eh {diferenca}')
