def trans_seconds (**kwargs):
    return f"{int(kwargs['hora'])*3600} {int(kwargs['minuto'])*60} {int(kwargs['segundo'])}"

paises = {'hora': '3', 'minuto': '4', 'segundo':30}
print(trans_seconds(**paises))