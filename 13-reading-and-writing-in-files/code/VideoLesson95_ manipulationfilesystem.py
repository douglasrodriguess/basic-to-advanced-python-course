"""
Manipulação de sistema de arquivos
"""
import os
from send2trash import send2trash
import tempfile

print("\n- Descobrindo se um arquivo existe ou nao")
print(os.path.exists("frutas.txt"))
print(os.path.exists("arquivao.txt"))

print("\n- Descobrindo se um diretorio existe ou nao")
print(os.getcwd())
os.chdir(".")
print(os.getcwd())
print(os.path.exists("geek"))
print(os.path.exists("code"))

print("\n- Criando um arquivo")
# open("creatfilewithmodew.text", "w").close()
# open("creatfilewithmodea.text", "a").close()
# with open("creatfilewithmodea.text", "a").close() as file:
#     pass
# os.mknod("creatfile.text")
# Se o arquivo via mkmod() já existir, terá o erro FileExistsError

print("\n- Criando um diretório únicos")
# os.mkdir("diretoriomkdir", exist_ok=True)
# É possível criar apenas um diretório por vez com o os.mkdir

print("\n- Criando vários diretórios")
# os.makedirs("diretoriomkdirs/directory1/directory2", exist_ok=True)

print("\n- Renomear diretórios")
# os.rename("diretoriomkdir", "diretoriomkdirnovo")
# # Se o diretório que deseja renomear não estiver vazio, teŕa um OSError

print("\n- Renomear arquivos")
# os.rename("/home/meupc/Desktop/basic-to-advanced-python-course-master/13-reading-and-writing-in-files/code/creatfile.text", "/home/meupc/Desktop/basic-to-advanced-python-course-master/13-reading-and-writing-in-files/code/creatfile1.text")

print("\n- Deleção de arquivos")
# os.remove("frutas.txt")

# Os arquivos não vão para lixeira, eles somem
# No windows, se o arquivo a ser deletado estiver sendo usado, será apresentado um erro

print("\n- Deleção de diretorios")
# os.rmdir("diretoriomkdirnovo")

print("\n- Removendo uma árvore de diretorios")
# print(os.getcwd())
# for arquivo in os.scandir("diretoriomkdirs"):
#    if arquivo.is_file():
#        os.remove(arquivo.path)

print("\n- Enviando arquivos para a lixeira")
# send2trash("creatfilewithmodea.text")
# send2trash("creatfilewithmodew.text")
# send2trash("novotexto.txt")
# send2trash("textox.txt")
# send2trash("texto.txt")

print("\n- Trabalhando com arquivos e diretórios temporários")
# Estamos criando um diretorio temporario, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto.
# No final, usamos um input() só para matermos os arquivos temporários 'vivos' dentro dos blocos with
# with tempfile.TemporaryDirectory() as tmp:
#     print("Criei o diretorio temporario em {0}".format(tmp))
#     with open(os.path.join(tmp, "arquivotemporario.txt"), "w") as arquivo:
#         arquivo.write(("Douglas\n"))
#         input()

print("\n- Trabalhando com arquivos temporários")
# Em arquivos temporários só é possível escrever bits
with tempfile.TemporaryDirectory() as tmp:
    tmp.write(b'douglas')
    tmp.seek(0)
    print(tmp.read())

