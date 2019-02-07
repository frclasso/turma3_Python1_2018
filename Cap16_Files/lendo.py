#!/usr/bin/env python3

fh = open('teste.txt', 'r') # read/leitura

# read le o arquivo inteiro
# linhas = fh.read()
# print(linhas)


# linhas = fh.readline()
# print(linhas)

linhas = fh.readlines(30)
for l in linhas:
    print(l, end='')
fh.close()


