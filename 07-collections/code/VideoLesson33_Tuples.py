"""
Tuplas (Tuple)

Diferenças de Tuplas com as Linhas:
    1. As tuplas são representadas por parênteses
    2. As tuplas são imutáveis

print(type([]))
print(type(()))

tupla1 = (1, 2, 3, 4)
print(tupla1)
print(type(tupla1))
tupla2 = (1, 2, 3, 4)
print(tupla2)
print(type(tupla2))

tupla3 = (4)  # Isso não é uma tupla, é um inteiro
print(tupla3)
print(type(tupla3))

tupla4 = (4, )
print(tupla4)
print(type(tupla4))

(4) -> não é tupla
(4, ) -> é tupla
4, -> é tupla

# CONCLUSAO: Tuplas são definidas pela vírgula e não pelo uso do parêntese

# Gerar tupla dinamicamente com range (inicio, fim passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desempacotamenteo de tupla
tupla = ('Douglas', 'Helena')
nome1, nome2 = tupla
print(nome1)
print(type(nome1))
print(nome2)

# Metodos de adição e remoção de elementos não existem nas tuplas

# Metodos de soma, máximo, mínimo e tamanho existem do mesmo modo que na Lista

# CONCATENAÇÃO DE TUPLAS
tupla1 = [1, 2, 3]
tupla2 = [4, 5, 6]
somatupla = tupla1 + tupla2
print(somatupla)
tupla1 = tupla1 + tupla2
print(tupla1)

# PROCURANDO UM ELEMENTO NA TUPLA
print(3 in tupla1)
print(33 in tupla1)

# INTERANDO SOBRE UMA TUPLA
for indice, valor in enumerate(tupla1):
    print(indice, valor)

# CONTANDO OS ELEMENTOS DE UM TUPLA
print(tupla1.count(1))

# DICAS DE UTILIZAÇÃO DE TUPLAS
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar
#    os dados contidos em uma coleção

meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)
print(meses[5])

i = 0
while i < len(meses):
    print(meses[i])
    i += 1

print(meses.index('Junho'))

# SLICE
meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses[5:9])

# Não há problema com shallow copy

# POR QUE UTILIZAR TUPLAS?
# - Tuplas são mais rápidas
# - Tuplas deixam seu código mais seguro
"""



