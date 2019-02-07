#!/usr/bin/env python3


# copiar uma imagem

with open('python.png', 'rb') as rf:
    with open('copia_de_python.png', 'wb') as wf:
        for line in rf:
            wf.write(line)




print('Feito...')