"""
ENTENDENDO **kwargs

# Exige parametros nomeados e transforma para dicionários
"""


def cores (**kwargs):
    for chave, cor in kwargs.items():
        print (f'A cor favorita de {chave} eh {cor}')
    return kwargs


print(cores (douglas='verde', wilton='branco'))


def cumprimento (**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um presente'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return "Nao tenho certeza quem voce e..."

print(cumprimento())
print(cumprimento(geek='Python'))
print(cumprimento(geek='teste'))


# Quando formos utilizar todos os tipos de parametros, temos que seguir a ordem: obrigatório -> *args -> *kwargs

def minha_funcao (idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casaso')
    print(kwargs)

# print(minha_funcao()) Erro


print(minha_funcao(23, 'Douglas', False))


###############################################################
# DESEMPACOTAMENTO

def mostra_nome(**kwargs):
    return f"{kwargs['nomes']} {kwargs['sobrenome']}"


nomeacao = {'nomes':'Douglas', 'sobrenome':'Rodrigues'}
print(mostra_nome(**nomeacao))


###################################################################
# COMPARANDO COLEÇÕES

def soma_multiplos(a, b, c):
    print(a+b+c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)


soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)
soma_multiplos(**dicionario) # chaves com os mesmos nomes que os parametros
