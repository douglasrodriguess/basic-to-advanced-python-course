"""
Loop com Break

Utilizamos o break para sair de loops de maneira projetada
"""

# break com for

for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print (numero)
print('Sai do loop')

# break com while

while True:
    comando = input('Digite sair para sair:')
    if comando == 'sair':
        break
