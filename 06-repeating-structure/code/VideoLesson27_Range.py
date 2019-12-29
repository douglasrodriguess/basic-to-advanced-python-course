"""
Ranges

Requisitos: entender for

Ranges: são utilizados para gerar sequencias numéricas de forma não aleatória e sim de forma esperada
    Forma 2: range
"""

# Forma prática:

"""    
    Forma 1: range(valor_de_parada)
        obs: valor_de_parada não inclusiva
"""

print('Forma 1')
for num in range(10):
    print(num)

"""    
    Forma 2: range(valor_de_inicio, valor_de_parada)
        obs: valor_de_parada não inclusiva
"""

print('Forma 2')
for num in range(2, 10):
    print(num)

"""    
    Forma 3: range(valor_de_inicio, valor_de_parada, passo)
        obs: valor_de_parada não inclusiva
        obs: passo específicado pelo usuário
"""

print('Forma 3')
for num in range(100, 110, 2):
    print(num)

"""    
    Forma 4: range(valor_de_inicio, valor_de_parada, passo)
        obs: valor_de_parada não inclusiva
        obs: passo específicado pelo usuário
"""

print('Forma 4')
for num in range(110, 100, -1):
    print(num)