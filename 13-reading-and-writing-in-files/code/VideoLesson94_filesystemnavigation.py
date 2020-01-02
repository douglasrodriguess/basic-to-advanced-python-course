"""
Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos de um sistema operacional, precisamos importar e fazer uso do modulo os
"""

import os
import sys

print("\n- Funcao getcwd")
# getcwd -> get current work directory
print(os.getcwd())

print("\n- Funcao chdir")
os.chdir('..')
print(os.getcwd())

print("\n- Checar se um diretório eh absoluto ou relativo")
print(os.path.isabs('/home/douglas/../'))

"""
Para usuários do Windows:
print(os.path.isabs('C:\\home\\douglas'))
"""

print("\n- Identificando o sistema operacional")
print(os.name)
# Output: posix (Linux) nt (windows)
print(os.uname())

print("\n- Identificando a plataforma")
print(sys.platform)

print("\n- Trabalhando com os.path.join()")
print(os.getcwd())
res = os.path.join(os.getcwd(), 'code')
os.chdir(res)
print(os.getcwd())

print("\n- Listando os arquivos")
print(os.getcwd())
print(os.listdir())

print("\n- Listando os arquivos com mais detalhes")
file = list(os.scandir())
print(file)
print(file[0])
print(file[0].inode())
print(file[0].name)
print(file[0].is_dir())
print(file[0].is_file())
print(file[0].is_symlink())
print(os.getcwd())
print(file[0].path)
print(file[0].stat())


