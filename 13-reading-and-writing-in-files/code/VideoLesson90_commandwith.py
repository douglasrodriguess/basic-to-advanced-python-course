"""
Bloco With é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with
"""

print('\n - Das aulas passadas...')
file = open('texto.txt')
print(file.read())
print(file.closed)
file.close()

print('\n - Forma pythônico de manipular arquivos')
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)

