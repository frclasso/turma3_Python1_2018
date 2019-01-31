#!/usr/bin/env python3

fh = open('numeros.txt', 'r') # read/leitura

# read le o arquivo inteiro
linhas = fh.read()

# linhas = fh.readlines()
for l in linhas:
    print(int(l), end=',')
#print(type(linhas))
fh.close()


