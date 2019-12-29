"""
Utilizando Lambdas:

- Conhecidas como funções lambdas ou, simplesmente, lambdas
- São funções sem nome ou funções anônimas

n = lambda x1, y1..., z1: <expressao>

"""
################################
print('Funcao em python')


def funcao (x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

print('Expressao em Lambda')

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

################################
print('Expressoes Lambdas com nenhuma entrada')
uma = lambda: 'Apenas uma entrada'
print(uma())

################################
print('Expressoes Lambdas com multiplas entradas')
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip: retira os espaços do início e fim de uma string

print(nome_completo('   douglAs',  'RODRIGUES'))

################################
print('Exemplo real do uso do Lambda')
autores = ['Douglas de Araujo Rodrigues', 'Roberto F. Ivo', 'Mariana Williams', 'Wilton do Nascimento', 'Itrio Netuno', 'Douglas Adams']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

################################
print('Lambda em funcoes')


def funcao_quadratica(a, b, c):
    return lambda x: a*x**2 + b*x + c


print(funcao_quadratica(2, 3, -5)(2))
