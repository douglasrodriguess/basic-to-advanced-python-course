"""
Video Lesson 89: Seek and Cursors

seek() é a função utilizada para movimentar cursors; essa função recebe como parâmetro pra onde o cursors deve ir

"""

arquivo = open('texto.txt')

print('\n - Primeira leitura do arquivo')
print(arquivo.read())

print('\n - Segunda leitura do arquivo')
print(arquivo.read())

print("\n- Movimentando um cursors")
arquivo.seek(0)
print(arquivo.read())

arquivo.close()

print("\n- Funcao que lê o arquivo linha a linha")
arquivo = open('texto.txt')
print(arquivo.readline())


print("\n- O retorno eh uma string, então estamos trabalhando com as funcionalidades de uma string")
ret = arquivo.read()
print(ret.split(' '))

arquivo.close()

print("\n- Cada linha é um elemento de uma lista")
arquivo = open('texto.txt')
print(arquivo.readlines())
linhas = arquivo.readlines()
print(len(linhas))

print("\n- Saber se o arquivo está aberto ou fechado")
# Retorna "False" se estiver aberto e "True" se estiver fechado
print(arquivo.closed)

print("\n- Fechar um arquivo")
arquivo.close()


