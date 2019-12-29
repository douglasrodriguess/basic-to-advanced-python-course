def informacoes(nome, sobrenome, idade, solteiro, **kwargs):
    print(f'Cliente: {nome} {sobrenome}')
    print(f'{nome} tem {idade} anos, portanto nasceu no ano de {2019-idade}')
    if solteiro:
        print(f'Estado civil do {nome} eh solteiro')
    else:
        print(f'Estado civil do {nome} eh casado')
    print(f"Localizacao: {localizacao['cidade']} / {localizacao['estado']} / {localizacao['pais']}")


nome = input('Digite o seu primeiro nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite sua idade: '))
solteiro = input("Estado civil - ('S') Solteiro e ('C') Casado: ")

if 'S' in solteiro:
    solteiro = True
else:
    solteiro = False

localizacao = {}
print(type(localizacao))
cidade = input('Digite sua cidade: ')
estado = input('Digite o seu estado: ')
pais = input('Digite o seu pais: ')
localizacao['cidade'] = cidade
localizacao['estado'] = estado
localizacao['pais'] = pais

informacoes(nome, sobrenome,idade, solteiro, **localizacao)
