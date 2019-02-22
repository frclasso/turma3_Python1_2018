#!/usr/bin/env python3


str = 'Python for Data Science'

print(str.split()) # parametro padrao espaco
print(str.split('a'))
print()

str2 = '*** Python *** for Data Science ***'
print(str2.strip('*')) #
print(str2.lstrip('*'))
print(str2.rstrip('*'))

# replace substituir strings
print(str.replace('Data Science', 'Big Data'))

voto = 'Haddad Presidente, Haddad do PT, '
print(voto.replace('Haddad', 'Bolsonaro',1))  # olhar

# find/encontrar
print(str.find('for'))
# index
print(str.index('for'))

