import datetime

year = datetime.date.today().year

idade = int(input(f'Quantos anos voce tem? '))
print(f'Voce nasceu em {datetime.date.today().year - idade}')
print(f'Data {datetime.date.today().day}/{datetime.datetime.today().month}/{datetime.datetime.today().year}')