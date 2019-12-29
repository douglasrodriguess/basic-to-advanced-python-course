"""
    Recebendo dados do usuário
"""

print("-"*40)
# Entrada de dados

"""
 input() => Todo dado recebido via input é do tipo String
 Em Python, string é tudo que estiver entre:
     - Aspas simples: 'Douglas'
     - Aspas duplas: "Douglas"
     - Aspas simples triplas: '''Douglas'''
     - Aspas duplas triplas: 
"""

print("Exemplo de entrada 'antigo' 2.x")
print("Qual seu nome? ")
nome = input()

print("Exemplo de entrada 'novo' 3.x")
nome = input("Qual seu nome? ")

#print("Exemplo de print 'antigo' 2.x")
#print{'Seja bem-vindo(a) %s' %nome}

print("Exemplo de print 'moderno' 3.x")
print('Seja bem-vindo(a) {0}!'.format(nome))

print("Exemplo de entrada 'antigo' 2.x")
print("Qual a sua idade? ")
idade = input()

print("Exemplo de entrada 'novo' 3.7 com o cast")
idade = int(input('Qual a sua idade?'))
"""
int(idade) => cast
cast é a 'conversão' de um tipo de dado para outro
"""

# Saída de dados
print("-"*40)

print("Exemplo de print 'antigo' 2.x")
print("A $s tem %d anos" %nome %idade)

print("Exemplo de print 'moderno' 3.x")
print('A {0} tem {1} anos'.format(nome, idade))

print("Exemplo de print 'mais moderno' 3.7")
print(f'O {nome} tem {idade} anos.')

print("Exemplo de print 'mais moderno' 3.7 com operação")
print(f'O {nome} nasceu em {2018 - int(idade)}.')


