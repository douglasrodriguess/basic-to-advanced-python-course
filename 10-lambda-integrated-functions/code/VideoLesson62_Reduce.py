"""
REDUCE

O que é método faz:
    funcao(funcao(funcao(...(funcao(a1, a2), a3), a4),..., an)

Características:
    Usar só quando for realmente utilizado
    99% das vezes o loop for é mais legível
    No reduce, a função tem que ter dois parâmetros de entrada
"""

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8]
multi = lambda x, y: x+y

res = reduce(multi, dados)
print(res)
