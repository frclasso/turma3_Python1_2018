#!/usr/bin/env python3


tup1 = ('Hist', 'Physics','Math','English')

# index
print(tup1[0])
print(tup1[-1])

# fatiar
print(tup1[1:])
print(tup1[::-1]) # inverte

# imutabilidade

list1 = ['Hist', 'Physics','Math','English']

list1[0] = 'Chemistry'
print(list1)

#tup1[0] = 'Chemistry'  # erro tuple' object does
# not support item assignment

tup1 = tup1[:2]
print(tup1)


tup3 = 1, # parenteses opcional, a virgula nao
print(type(tup3))
print(len(tup1))

tup4 = tuple(list1)
print(tup4)

print(max(tup4))
print(min(tup4))

