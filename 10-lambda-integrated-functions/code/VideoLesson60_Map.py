"""
Map

Com Map, fazendo o mapeamento de valores para função

Estrutura:
    dados: a1, a2, a3, a4, ..., an
    funcao: f(x)
    funcao map (f, dados)

Obs: Após a primeira utilização do map com o resultado, ele zera
"""
#########################################
import math

print('Exemplo usando funcoes')


def funcao_area(r):
    return math.pi*(r**2)


area = []
raios = [1, 2, 3, 4, 5]
for r in raios:
    area.append((funcao_area(r)))
print(area)


print('Exemplo usando maps')
area = map(funcao_area, raios)
print(list(area))

print('Exemplo usando maps e lambdas')
print(list(map(lambda r: math.pi*(r**2), raios)))

#####################################################
print('Mais um exemplo')
cidades = [('Fortaleza', 23), ('Berlin', -23)]
c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)
print(list(map(c_para_f, cidades)))
