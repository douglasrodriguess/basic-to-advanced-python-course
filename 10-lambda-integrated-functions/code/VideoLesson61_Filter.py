"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

filter(função, iteravel)
"""
########################################################
print('Exemplo do uso do Filter')


import statistics

dados = [1.2, 1.5, 1.5, 7.5, 3.5, 3.9]
media = statistics.mean(dados)
print(media)
media = sum(dados)/len(dados)
print(media)

res = filter(lambda x: x>media, dados)
print(list(res))

# Assim como na função map, após serem utlizados os valores de filter, os valores são removidos da memória
print(list(res))

########################################################
print('Exemplo do uso do Filter')
paises = ['', 'Brasil', 'Portugal', 'Espanha', 'Holanda', '', '']
print(paises)
test = filter(None, paises)
print((list(test)))
test = filter(lambda pais: len(pais) > 0, paises)
print((list(test)))
test = filter(lambda pais: pais != '', paises)
print((list(test)))

########################################################
print('No filter(), a funcao retorna True ou False')
print('No map(), a funcao retorna um objeto. Pode ter a funcao de filtrar')

########################################################
print('Exemplo mais complexo')

usuario = [
    {'username': 'Douglas', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']},
    {'username': 'Renato', 'tweets': []},
    {'username': 'Vitoria', 'tweets': ['Eu adoro refrigerante']},
    {'username': 'Helena', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']},
    {'username': 'Florinda', 'tweets': []},
    {'username': 'Flavio', 'tweets': ['Eu adoro salgado']}
]
print(usuario)
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuario))
print(inativos)
# O vazio é falso
inativos = list(filter(lambda u: not u['tweets'], usuario))
print(inativos)
ativos = list(filter(lambda u: len(u['tweets']) != 0, usuario))
print(ativos)

print('##################################################################')
print('Combinando filter() e map()')

nomes = ['Maria', 'Ana', 'Florinda']
lista = list(map(lambda nome: f'Sua estrutua eh {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)