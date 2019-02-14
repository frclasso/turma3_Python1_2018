#/usr/bin/env python3

# IOError

try:
    fh = open('testefile.txt', 'r')
    fh.read()
except IOError:
    print('Arquivo nao encontrado')
else:
    print('Arquivo encontrado com sucesso')
    fh.close()