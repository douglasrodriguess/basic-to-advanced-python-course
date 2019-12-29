"Try and Except servem para tratar erros no código"
"""Estrutura:
try:
    execução problemática
except:
    tratando o problema   
"""

print("-"*40)
print("[1] - Exemplo da estrutura do uso do try/except")
try:
    test()
except:
    print("Deu um erro!")

print("-"*40)
print("[2] - Tratando um erro específico")
print("A dica é tratar um erro específico, e não um erro genérico")
try:
    test()
except NameError:
    print("Esta sendo usado uma funcao inexistente")

try:
    len(5)
except TypeError:
    print("Esta sendo usado uma funcao inexistente")

print("-"*40)
print("[3] - Tratando um erro específico com detalhes da descricao")
try:
    test()
except NameError as err:
    print(f'O codigo apresentou o seguinte erro: {err}')

print("-"*40)
print("[4] - Tratando varios erros específicos com detalhes da descricao")
try:
    # test()
    # len(4)
    print('Name'[9])
except NameError as erra:
    print(f'Erro: {erra}')
except TypeError as errb:
    print(f'Erro: {errb}')
except:
    print("Deu um erro diferente")

print("-"*40)
print("[5] - Tratando erros em funcoes")

def tratando_erros (dicionario, valor):
    try:
        return dicionario[valor]
    except TypeError:
        return None
    except NameError:
        None
    except IndexError:
        None

dic = {"nome": "Douglas"}

print(tratando_erros(dic,"nome"))
print(tratando_erros(9,"nome"))
print(tratando_erros("nome", 4))