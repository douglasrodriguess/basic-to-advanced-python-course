import os
import sys

with open("texto01.txt", "w") as file:
    try:
        while True:
            caract = input("Digite caracteres: ")
            if caract != "0":
                file.write(caract + "\n")
            else:
                file.close()
                break
    except TypeError:
        print("Nao foi escrito uma string")


with open("texto01.txt") as fileread:
    print("Imprimindo o arquivo {0}".format(fileread.name))
    print(fileread.read())
    fileread.close()
