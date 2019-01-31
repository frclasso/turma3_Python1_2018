#!/usr/bin/env python3

# abrindo
file = open('teste.txt', 'w')
# print(file.name)
# print(file.mode)
# print(file.closed)

# escrevendo
file.write('Uma linha')

file.write('\nSegunda linha')
file.write('\nMais uma linha')
file.write('\nQuarta linha')
file.write('\nQuintta linha')
file.write('\nSexta linha')
file.write('\nSetima linha')
file.write('\nOitava linha')

file.close()

print(file.closed)