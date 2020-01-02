"""
Modos de abertura de arquivo

'x' -> abre para escrita somente se o arquivo não existir. Caso exista, retorna um FileExistsError
'a' -> o conteudo é adicionado sempre no final do arquivo
'+' -> abre para a atualização, seja de leitura ou escrita
'r+' ou 'w+' -> há o controle do cursor

link: https://docs.python.org/3/library/functions.html#open
"""

print("\n - Modo de abertura 'w'")
with open('frutas.txt', 'w') as file:
    try:
        while True:
            frutas = input("Digite uma fruta ou a palavra 'sair': ")
            if frutas != 'sair':
                file.write(frutas + '\n')
            else:
                break
    except TypeError:
        print("A funcao recebe apenas string como parametro")
with open('frutas.txt') as file:
    print(file.read())
    file.close()

print("\n - Modo de abertura 'a'")
with open('frutas.txt', 'a') as file:
    try:
        while True:
            frutas = input("Digite uma fruta ou a palavra 'sair': ")
            if frutas != 'sair':
                file.write(frutas + '\n')
            else:
                break
    except TypeError:
        print("A funcao recebe apenas string como parametro")
with open('frutas.txt') as file:
    print(file.read())
    file.close()

print("\n - Modo de abertura 'r+'")
with open('frutas.txt', 'r+') as file:
    try:
        while True:
            file.seek(24)
            frutas = input("Digite uma fruta ou a palavra 'sair': ")
            if frutas != 'sair':
                file.write(frutas + '\n')
            else:
                break
    except TypeError:
        print("A funcao recebe apenas string como parametro")
with open('frutas.txt') as file:
    print(file.read())
    file.close()
