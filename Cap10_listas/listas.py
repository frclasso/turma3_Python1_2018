#!/usr/bin/env python3



#listas

mylist = [10, 20, 30, 'spam', 'ham', 'eggs']

# indexar
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
# fatiar
print(mylist[:3])
print(mylist[3:])
# concatenar
print(mylist + ['apple', 'grapes'])
# modificar, listas sao mutaveis
mylist[0] = 1000
print(mylist)

# deletar

# pop(indice)
mylist.pop(0)
print(mylist)
# remove(valor)
mylist.remove('eggs')
print(mylist)
# del(indice)
del mylist[-1]
print(mylist)

# del mylist
# print(mylist)

