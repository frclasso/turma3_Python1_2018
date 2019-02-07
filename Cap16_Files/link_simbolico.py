#!/usr/bin/env python3


# Criando um atalho / simbolic link

origem = ('/Users/fabio/Desktop/turma3_Python1_2018/'
          'Cap16_Files/imgs')

simbolic_link = ('/Users/fabio/Desktop/imgs_atalho')

import os
os.symlink(origem, simbolic_link)

print("Atalhos criado com sucesso")