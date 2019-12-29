num = float(input("Digite um numero: "))

if num == int(num):
    print(f'O somatorio do sucessor do seu triplo com o antecessor de seu dobro eh {(num*3)+1 + (num*2)-1}')
else:
    print("O numero nao eh inteiro")
