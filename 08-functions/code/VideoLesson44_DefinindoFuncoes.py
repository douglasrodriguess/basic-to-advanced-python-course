"""
DEFININDO FUNÇÕES

- Funções são partes de códigos que realizam tarefas específicas
- As funções podem ou não receber e entregar (na saída) dados

- Uma função intergrada do python é chamada de Built-in
- DRY - Don't Repeat Yourself (Não repita o seu código / Não repita você mesmo)
"""

##############################################################
# DEFINICAO DE FUNCOES
print()
print('-'*30)
print('DEFINICAO DE FUNCOES')
print()

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

"""
- Palavra reservada do python para funcao é o "def"
- SEMPRE minusculo e se for composto, deve ser separado com o underline
- Pode ou nao receber parametros de entrada
- No bloco da funcao pode ou nao ter o retorno da funcao
"""

# Declaração
def cantar_parabens():
    print("Hora de cantar parabens")

# Transferencia da execucao da funcao
#A variável recebe a execucao da atividade da funcao variavel
canta = cantar_parabens

# Executando
canta()