#!/usr/bin/env python3

str = 'Python 3 for Data Science'

contador = 0
for x in str:
    if x == 'a':
        contador += 1
print(contador)

# Usando a funcao count()
print(str.count('a'))

# classificar

print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.isdigit())  # nao é digito False
print(str.isupper()) # nao é upper case False
print(str.swapcase()) # inverte o case
print()


def ehMinusculo(ch):
    return ch in str.lower()


print(ehMinusculo('S'))
print(ehMinusculo('s'))

maiusculo = lambda x:x.upper()
print(maiusculo('a'))