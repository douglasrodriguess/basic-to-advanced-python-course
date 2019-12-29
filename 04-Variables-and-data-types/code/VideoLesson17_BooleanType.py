"""
    Tipo Booliano

Álgebra Boolenana

Duas constantes:

True -> Verdadeiro
False -> Falso

Errado
true, false

Certo
True, False
"""

ativo = True

print(ativo)

"""
   Operação básica: Negação (not): se o valor for verdadeiro, o resultado da negação vai ser falso
     já se o valor for falso, o resultado da operação vai ser verdadeiro
"""

print(not ativo)

"""
   Operação básica: Ou (or): operação binária, ou seja, depende de dois valores. 
       Ou um outro outro deve ser verdadeiro
       
       True or True -> True
       True or False -> True
       False or True -> True
       False or False -> False
"""

logado = False

print(ativo or logado)

"""
   Operação básica: And (and): operação binária, ou seja, depende de dois valores. 
       Ambos os valores devem ser verdadeiros

       True or True -> True
       True or False -> False
       False or True -> False
       False or False -> False
"""

print (ativo and logado)

print(bool(0))
print(bool(1))
print(bool(100))
print(bool(10))