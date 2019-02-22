#/usr/bin/env python3

try:
    fh = open('testefile.txt', 'w')
    fh.write('This is my teste')
finally:
    print('Error, nao foi possivel ler ou encontrar o arquivo')
    fh.close()
