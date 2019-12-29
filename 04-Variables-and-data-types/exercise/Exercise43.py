# Escreve um programa para ajudar vendedores

valor = float(input('Digite o valor da compra: '))
case1 = valor - valor*0.10
print(f'Valor a vista: R$ {case1}')
case2 = valor/3
print(f'Valor da parcela: R$ {case2:.2f}')
case3 = case1*0.05
print(f'Comissao do vendedor se for a vista: R$ {case3}')
case4 = valor*0.05
print(f'Comissao do vendedor se for parcelado: R$ {case4}')
