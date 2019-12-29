# Algoritmo que calcula o IMC

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em m: '))

IMC = peso/(altura**2)

print(f'O IMC eh {IMC}')
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.6 and IMC <= 24.9:
    print('Saudavel')
elif IMC >= 25 and IMC <= 29.9:
    print('Saudavel')
elif IMC >= 30 and IMC <= 34.9:
    print('Obesidade Grau I')
elif IMC >= 35 and IMC <= 39.9:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (morbida)')