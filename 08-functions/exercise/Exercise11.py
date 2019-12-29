import statistics

def media(num, nome):
    """
    Funcao que calcula a media
    :param num: lista de numeros que serao realizados para o calculo da media
    :param nome: parametro de escolha se e media ponderada ('P') ou aritmética ('A')
    :return: retorna a media
    """
    if nome == 'A':
        media = statistics.mean(num)
        return media
    media = (5*num[0] + 3*num[1] + num[2])/10
    return media


num = []
for i in range(4):
    if i < 3:
        nota = float(input(f'Digite a nota {i}: '))
        num.append(nota)
    else:
        nome = input('Digite a operacao (A) Media aritmetica (P) Media ponderada: ')
print(f'Sua media eh {media(num, nome)}')
