"""
Conjuntos:
    São chamados de Sets em Python
    Não possuem valores duplicados
    Não possuem valores ordenados
    Não são indexados, ou seja, não são acessados via índice

Representação por {}

Quando utilizar?
    Precisamso armazenas elementos, mas não vamos nos preocupar com ordem, duplicação...

"""

##############################################################
# DEFININDO UM CONJUNTO

# Forma 1

c = set({1, 2, 3, 4, 5, 10, 1, 2, 5})
print(c)
print(type(c))

# Ao criar um conjunto e este conter números repetidos, será repassado realmente para o conjunto apenas o uma vez
#   aquele valor repetido.

c = {1, 2, 3, 4, 5, 10, 1, 2, 5}
print(c)
print(type(c))

##############################################################
# DEFININDO UM CONJUNTO

if 3 in c:
    print("Esta no conjunto")
else:
    print("Nao esta no conjunto")

# Lista aceitam valores duplicado
lista = [1, 2, 10, 4, 5, 3, 1, 2, 5]
print(lista)
print(type(lista))
# Tuplas aceitam valores duplicado
tupla = (1, 2, 3, 4, 5, 10, 1, 2, 5)
print(tupla)
print(type(tupla))
# Dicionário não aceitam chaves duplicadas
dicionario = {}.fromkeys([1, 2, 10, 4, 5, 3, 1, 2, 5], 'dict')
print(f'Lista: {dicionario}')
print(type(dicionario))
# Dicionário não aceitam valores duplicado
conjunto = {1, 2, 3, 4, 5, 10, 1, 2, 5}
print(conjunto)
print(type(conjunto))

##############################################################
# TIPOS DE DADOS E ITERAÇÃO

# Podemos usar todo tipo de conjunto de dados
s = {3, 5, 6, True, 'b'}

# Iteração
for k in s:
    print(k)

##############################################################
# ESTUDO DE CASO

lista = ['Fortaleza', 'Maracanau', 'Fortaleza', 'Maranguape', 'Quixada']
print(f'Numero de cidades eh {len(set(lista))}')

##############################################################
# ADICIONANDO ELEMENTOS NOS CONJUNTOS

s = {1, 3, 5}

s.add(4)
s.add(1) # Adicionar um valor já existente não ocacionsa erro
print(s)

##############################################################
# REMOVENDO ELEMENTOS NOS CONJUNTOS

s = {1, 3, 5}
print(s)

# Forma 1

ret = s.remove(3)
print(s)
print(ret)
#s.remove(10) # Remover um elemento que tá na lista, ocasiona erro
# Nao retorna nenhum valor

# Forma 2

s.discard(1)
print(s)

# Se o valor nessa Forma 2 não for encontrado, nenhum erro será retornado

##############################################################
# LIMPANDO UM CONJUNTO

s = {1, 3, 5}
print(s)

s.clear()

print(s)

##############################################################
# COPIANDO UM CONJUNTO PARA OUTRO

# Forma 1 (Deep Copy): totalmente separados, independentes
#    Faz um novo espaço na memória e aloca as coisas pra lá

s = {1, 3, 5}
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 (Shallow Copy):

novo = s
print(novo)

novo.add(4)

print(novo)
print(s)

##############################################################
# OPERAÇÕES COM CONJUNTOS
print()
print('-'*30)
print('OPERACOES COM CONJUNTOS')
print()

cursopython = {'Douglas', 'Alysson', 'Vitoria', 'Joao', 'Gesi'}
cursojava = {'Douglas', 'Guilherme', 'Vitoria'}

# UNIAO
# Forma 1:

unico1 = cursopython.union(cursojava)
print(unico1)

# Forma 2: Usando caractere pipe |

unico2 = cursopython | cursojava
print(unico2)

# INTERSEÇÃO
# Forma 1:

intersecao1 = cursojava.intersection(cursopython)
print(intersecao1)

# Forma 2: Usando &

intersecao2 = cursopython & cursojava
print(intersecao2)

# DIFERENÇA

diferenca1 = cursojava.difference(cursopython)
print(diferenca1)
