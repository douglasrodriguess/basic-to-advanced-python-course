import os
import sys

print(os.name)
print(os.uname())
print(sys.platform)
if not os.path.exists("arquivo.txt"):
    end = os.path.join(os.getcwd(), "arquivo.txt")
    with open(end, "w") as file:
        os.makedirs("resultados/pessoa1", exist_ok=True)
        file.close()
        os.remove("arquivo.txt")
else:
    print("O arquivo já existe")


