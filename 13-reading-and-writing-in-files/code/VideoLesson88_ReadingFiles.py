"""
Leitura de arquivos
"""

"""
Função open(): na forma mais simples é passado apenas um parâmetro (arquivo ou endereço) que é o arquivo a ser lido 
(obrigatório). Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

Por padrão, a função open() abre o arquivo para leitura. Esse arquivo deve existir, caso contrário vai ter o erro 
FileNotFounderError
"""

print("Abrindo um arquivo...")
arquivo = open('texto.txt')

print("print no arquivo")
print(arquivo)
"<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>"
"mode = r (quer dizer que o arquivo foi abertosó para leitura)"

print("Type do arquivo")
print(type(arquivo))

print("Lendo um arquivo")
print(arquivo.read())


