#!/usr/bin/env python3


# seek  - define a posicao do cursor
# tell - informa a posicao do cursor
f = open('teste.txt', 'r')
str = f.read(28)
print('Lendo:', str)
position = f.tell()
print('Posição atual do cursor:', position)


#inicio = f.seek(0,0)
str = f.read(28)
print('Lendo novamente...', str)
position = f.tell()
print('Posição atual do cursor:', position)
