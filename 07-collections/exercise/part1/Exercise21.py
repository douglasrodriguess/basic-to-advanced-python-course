valorA = float(input('Insira o valor correspondente a A: '))
valorB = float(input('Insira o valor correspondente a B: '))

recolocacao = {'A':valorA, 'B':valorB}
print(recolocacao)
print(type(recolocacao))

C = recolocacao.get('A') - recolocacao.get('B')
print(C)
