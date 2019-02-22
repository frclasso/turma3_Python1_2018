#!/usr/bin/env python3


# renomeando um arquivo

# módulo os permite usarmos funcoes do sistema operacional
import os

# listar subdiretorios

for root, dirs, files in os.walk("/Users/fabio/Desktop/turma3_Python1_2018", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))


print('Feito...')