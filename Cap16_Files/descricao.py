#!/usr/bin/env python3


# arquivos
# funcao open('nome do arquivo com extensao', 'modo de abertura')

# fh = open('teste.txt','w') # write/escrita
#
# print('Tudo certo')
# fh.close()

# funcao with + open()
with open('outro_teste.txt', mode='w') as fh:
    pass

print('Ok...')