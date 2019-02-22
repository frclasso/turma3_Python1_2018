#!/usr/bin/env python3


def findCh(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice += 1
    return indice


print(findCh('Python for Data Science','S'))

# Usando Python Tools
str = 'Python Developer'
print(str.find('D'))