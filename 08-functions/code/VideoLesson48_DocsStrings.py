"""
DOCUMENTANDO FUNÇÕES COM DOCSSTRINGS

Podemos ter acesso a documentação de uma função usando no terminal:
- nome.__doc__
- help(nome)
"""


def diz_oi():
    """Uma funcao que retorna 'Oi'"""
    return 'Oi'


def exponencial(numero, potencia):
    """
    Funcao que retorna por padrao o quadrado do 'numero' á 'potencia' informada
    :param numero:
    :param potencia:
    :return:
    """
    return numero**potencia