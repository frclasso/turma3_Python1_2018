#!/usr/bin/env python3


# funcao open Cap 16 - arquivos

# open, nome do arquivo, modo de abertura

f = open('teste.txt', 'w') # w /write /escrever
f.write('Primeira linha do arquivo')

f.close() # open/close


with open('outro.txt', mode='w') as f:
    f.write('Primeira linhas de outro arquivo')