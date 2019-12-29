"""
PEP8 - Python Enhancement Proposals

São propostas as melhorias para a linguagem Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

---------------------------------------------------------------------------------
[1] - Utilize Camel Case para nomes de classes:
      [1.1] Se o nome for junto, utilize letra maiuscula para cada palavra.
            class CalculadoraCientifica:
                pass
      [1.2] Se for só um nome, este deve começar com letra maiuscula:
            class Calculadora:
                pass

---------------------------------------------------------------------------------
[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis
       def soma():
            pass
       def soma_dois():
            pass
       numero = 4
       numero_impar = 4

---------------------------------------------------------------------------------
[3] - Utilize 4 espaços para identação! (Não use o tab):
    if 'a' in 'banana':
        print('ten')

---------------------------------------------------------------------------------
[4] - Linhas em branco:
      [4.1] Separar funções e definições de classe com duas linhas em branco de uma classe
      [4.2] Métodos dentro de uma classe devem ser separados com uma única linha em branco

---------------------------------------------------------------------------------
[5] - Imports:
      [5.1] Devem ser sempre feitos em linhas separadas:
            import sys (certo)
            import sys, os (errado)
            from types import StringType, ListType (errado)
            from types import {
                StringType,
                ListType,
                SetType,
                OutroType
            }

      [5.2] Devem ser colocados no topo do arquivo, logo depois de quaisquer comentários
      ou docstrings e antes de constantes ou variáveis globais

---------------------------------------------------------------------------------
[6] - Espaços em expressões e instruções

funcao( algo[ 1 ], { outro: 2 } } (errado)
funcao(algo[1], {outro= 2}} (certo)
direc['chave'] = lista[indice] (certo)
x = 1 (certo)
x    = 1 (errado)

---------------------------------------------------------------------------------
[7] - Termine sempre uma instrução com uma nova linha
"""
import this







