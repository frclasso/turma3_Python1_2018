#!/usr/bin/env python3


# copiar o conteudo de um arquivo txt

with open('loren_ipsum.txt', 'r') as rf:
    with open('copia_de_loren.txt', 'w') as wf:
        for line in rf:
            wf.write(line)



print('Feito...')