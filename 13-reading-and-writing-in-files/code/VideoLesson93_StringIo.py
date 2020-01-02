"""
StringIO

Para ler ou escrever dados em arquivos em um SO, o software precisa ter permissão:
    - Permissão de leitura
    - Permissão de escrita

StringIO: utilizado para ler e criar arquivos em memória

"""

from io import StringIO

mensagem = 'Este eh um teste do uso de StringIO\n'

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write("Bem interessante a possibilidade de criar um arquico apenas na memoria do SO")

arquivo.seek(0)
print(arquivo.read())
