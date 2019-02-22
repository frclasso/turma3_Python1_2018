#!/usr/bin/env python3


# renomeando um arquivo

# módulo os permite usarmos funcoes do sistema operacional
import os

# listar conteudo do diretoruo
conteudo = os.listdir() # pode-se definir um caminho - PATH
for c in conteudo:
    print(c)

print('Feito...')