#!/usr/bin/env python3


import string

# splti () separa
poesia = "O orvalho no carvalho"
print(poesia.split())

# join() junta
print(''.join(poesia))




# convertendo

str = 'Python'
print(list(str))

tupla = (1,2,3,4,56)
print(list(tupla))

num = {1,2,3,4}  #set
print(list(num))

lista = [1,2,33,4]
lista.reverse()
print(lista)

# index

print(lista[1])
print(lista.index(33))