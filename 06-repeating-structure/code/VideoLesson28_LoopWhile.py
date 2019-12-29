"""
Loop While

Forma geral:
while expressao_booliana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressao booleana: é toda expressao onde o resultado é verdadeiro ou falso:

"""

numero = 1
while numero<10:
    print(numero)
    numero += 1

# Em um loop while é importante que cuidemos do critério de parada

resposta = ''
while resposta != 'sim':
    resposta = input('Ja acabou Jessica?')

