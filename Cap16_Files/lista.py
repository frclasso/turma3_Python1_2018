#!/usr/bin/env python3

fh = open('numeros.txt', 'w')
for n in range(10):
    fh.write(str(n) + '')
fh.close()