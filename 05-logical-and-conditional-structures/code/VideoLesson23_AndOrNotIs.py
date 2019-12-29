"""
Estruturas lógicas: and, or, not, is

Operadores unários: not
Operadores binários: and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
Para 'is', o valor é comparado com um segundo valor
"""

ativo = True
logado = True

if ativo and logado:
    print("[1] Bem-vindo, usuário.")
else:
    print("[1] Voce precisa ativar sua conta. Por favor, cheque o email")

ativo = True
logado = True

if ativo or logado:
    print("[2] Bem-vindo, usuário.")
else:
    print("[2] Voce precisa ativar sua conta. Por favor, cheque o email")

ativo = False
logado = True

# Se não estiver ativo faça isso aqui...
if not ativo:
    print("[3] Voce precisa ativar sua conta. Por favor, cheque o email")
else:
    print("[3] Bem-vindo, usuário.")

print(not False)

ativo = False

if ativo is False:
    print("[3] Voce precisa ativar sua conta. Por favor, cheque o email")
else:
    print("[3] Bem-vindo, usuário.")

print(ativo is True)

"""
Terminal:
    nome = 'Douglas'
    nome.istitle()
    True
    nome.title().istitle()
    True
    nome.title()
    'Douglas'         
"""

