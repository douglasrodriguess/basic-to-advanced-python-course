def operacao(*args):
    """
    Funcao que realiza as quatro operacoes matematicas
    :param num: lista de numeros para a operacao
    :param args: operacao matematica escolhida
    :return: retorna o resultado a operacao escolhida
    """
    if '+' in args:
        return num[0] + num[1]
    elif '-' in args:
        return num[0] - num[1]
    elif '*' in args:
        return num[0]*num[1]
    return num[0]/num[1]


num = []
for i in range(3):
    if i < 2:
        nota = float(input(f'Digite o numero {i}: '))
        num.append(nota)
    else:
        nome = input('Digite a operacao matematica: ')
print(f'Sua media eh {operacao(*num, nome)}')
