"""
Escrevendo em arquivos
"""

import numpy as np

# Ao abrir um arquivo para leitura, não é possível realizar a leitura. Do mesmo modo no contrário.
with open('texto.txt', 'w') as file:
    file.write("Escrever dados em arquivo eh muito facil\n")
    file.write("Esta eh a ultima linha\n")
    file.close()
with open('texto.txt') as file:
    print(file.read())
    file.close()

print("\n - Ao escrever em um arquivo que nao existe, eh criado um no SO")
with open('novotexto.txt', 'w') as file:
    file.write("Escrever dados em arquivo eh muito facil\n")
    file.write("Esta eh a ultima linha\n")
    file.close()
with open('novotexto.txt') as file:
    print(file.read())
    file.close()

print("\n - A funcao recebe apenas string como parametro")
with open('novotexto.txt', 'w') as file:
    try:
        file.write("Escrever dados em arquivo eh muito facil\n")
        file.write("Esta eh a ultima linha\n")
        file.write(23)
        file.close()
    except TypeError:
        print("A funcao recebe apenas string como parametro")
with open('novotexto.txt') as file:
    print(file.read())
    file.close()

print("\n - Recebendo informacoes de um usuario")
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
