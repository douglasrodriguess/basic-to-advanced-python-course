"""
    Tipo float

    Tipo real, decimal

    O separador de casas decimais na programação é o ponto e não a virgula
"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 23
print(valor)
print(dir(valor))
print(type(valor))

# Certo do ponto de vista do float
valor = 1.24
print(valor)
print(type(valor))

# Converter de float para int (vice-versa)
# Ao fazer essa conversão, são perdidos a precisão
res = int(valor)
print(res)
print(type(res))

# É possível fazer dupla atribuição
valor0, valor1 = 1, 33
print(valor0)
print(type(valor0))
print(valor1)
print(type(valor1))

# Números complexos
variavel = 5j
print(variavel)
print(type(variavel))
print(variavel ** 2)
