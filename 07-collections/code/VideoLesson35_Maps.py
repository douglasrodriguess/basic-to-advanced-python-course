##############################################################
"""
MAPAS em Python são chamadas de dicionários (representação em {})

"""

##############################################################
# TRABALHANDO DE FORMA ITERÁVEL

receita = {'jan': 1, 'fev': 2, 'mar': 3}
print(receita)

for id in receita:
    print(id)

for id in receita:
    print(receita[id])

##############################################################
# ACESSANDO AS CHAVES

print(receita.keys())

for id in receita.keys():
    print(receita[id])

print(receita.values())

##############################################################
# DESEMPACOTAMENTE DE VALORES

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

##############################################################
# OPERAÇÕES BÁSICAS

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))