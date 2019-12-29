##############################################################
"""
DICIONARIOS (MAPAS): são coleções do tipo chave/valor
Nas listas e nas tuplas, as chaves ficam implicitas, diferentemente dos dicionários
Os dicionário são representados por chaes {}
print(type([]))
print(type(()))
print(type({}))
OBS: Sobre dicionários:
    - a chave e o valor são separados por :
    - tanto a chave como o valor podem ser de qualquer tipo de dado
    - podemos misturar tipos de dados diferentes
"""

##############################################################
# FORMAS DE CRIAÇÃO

# Forma 1:

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)
print(type(paises))

# Forma 2:

paises = dict(br = 'Brasil', eua = 'Estados Unidos')
print(paises)
print(type(paises))

##############################################################
# ACESSANDO ELEMENTOS

# Via chave
paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises['eua'])
# print(paises.get['ru'])  # Resulta em um erro

# Via get (RECOMENDADO)
print(paises.get('br'))
print(paises.get('ru'))

# Caso não seja encontrado o objeto, retornará o tipo None
pais = paises.get('ru')
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f'Nao encontrei o pais')

# Definindo um valor padrão, caso não seja
#     encontrado o objeto com a chave informada
pais = paises.get('ru', 'Nao encontrado')
print(f'Encontrei o pais {pais}')

##############################################################
# VERIFICANDO ALGO NO DICIONÁRIO

paises = {'br':'Brasil', 'eua':'Estados Unidos'}

print('br' in paises)

if 'ru' in paises:
    russia = paises('ru')

##############################################################
# UTILIZANDO VARIOS TIPOS DE DADOS

localidade = {(43.2422,342.244): 'Escritorio em Toquio',
(24.2242, 242.1223): 'Escritorio em Sao Paulo'}
print(localidade)

##############################################################
# ADICIONAR ELEMENTOS EM UM DICIONÁRIO

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

# Forma 1 (Mais usual)
receita['abr'] = 400
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

##############################################################
# ATUALIZANDO DADOS EM UM DICIONÁRIO

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 700})
print(receita)

# Não podemos ter chaves repetidas
# Para adicionar ou atualizar um elemento, é utilizado o mesmo modo

##############################################################
# REMOVER DADOS DE UM DICIONÁRIO

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

# Forma 1 (+ comum)
ret = receita.pop('mar')
print(receita)

# Forma 2
del receita ['fev']
print(receita)

##############################################################
# FORMAS DE CRIAÇÃO

# Forma 1:

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)
print(type(paises))

# Forma 2:

paises = dict(br = 'Brasil', eua = 'Estados Unidos')
print(paises)
print(type(paises))

##############################################################
# ACESSANDO ELEMENTOS

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises['eua'])


##############################################################
# QUANDO USAR DICIONÁRIOS

# Usando Listas

carrinho = []

produto1 = ['Arroz', 1, 2,50]
produto2 = ['Feijao', 2, 5.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Usando Tuplas

carrinho = ()

produto1 = ('Arroz', 1, 2,50)
produto2 = ('Feijao', 2, 5.00)

carrinho = (produto1, produto2)

print(carrinho)

# Usando Dicionários

carrinho = []

produto1 = {'produto':'Arroz', 'quantidade':1, 'preco': 2.50}
produto2 = {'produto':'Feijao', 'quantidade':2, 'preco': 5.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

##############################################################
# COPIANDO

chave = dict(a=1, b=2, c=3)
print(chave)
print(type(chave))

# Forma 1: Deep Copy

novo0 = chave.copy()
print(novo0)
novo0['d'] = 4
print(novo0)

#Forma 2: Shallow Copy
novo1 = novo0
novo1['e'] = 5
print(novo1)
print(novo0)


##############################################################
# APAGANDO UM DICIONÁRIO

chave.clear()
novo0.clear()
novo1.clear()
print(chave)
print(novo0)
print(novo1)


##############################################################
# CRIANDO UM DICIONÁRIO DE MODO NÃO USUAL

# Forma 1:

outro = {}.fromkeys('a', 2)
print(outro)
print(type(outro))

# Forma 2:

usuario = {}.fromkeys(['nome', 'idade', 'cidade'], 'desconhecido')
print(usuario)
print(type(usuario))


##############################################################
# TRABALHANDO DE FORMA ITERÁVEL

# Forma 1:

outro = {}.fromkeys('teste', 'valor')
print(outro)
print(type(outro))

# Forma 2:

outro = {}.fromkeys(range(1, 11), 'valor')
print(outro)
print(type(outro))


