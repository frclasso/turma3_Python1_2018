#!/usr/bin/env python3


# -*-coding:utf-8 -*-


myString = "Hello Python course"

# indexar
print(myString[0])
print(myString[1])
print(myString[-1])
print(myString[-2])
print(myString.index('course'))
print(myString[13])

# fatiar /slicing [:]
print(myString[:5])

# concatenar  operador +
newString = '2018'
print(myString + ' ' + newString)

# inverter
print(myString[::-1])

# alterar
outraString = myString[:6] + 'Julia language'
print(outraString)

# iterar
for x in myString:
    print(x, end='')


# numerar
for x in enumerate(myString):
    print(x)