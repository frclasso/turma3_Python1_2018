#!/usr/bin/env python3

# set deafult method
# dois valores, chave / valor padrao

dict = {'Name': 'Zara', 'Age':32}

print('Valor:{}'.format(dict.setdefault('Age', None)))
print('Valor:{}'.format(dict.setdefault('Sex', 'Male')))
print('Valor:{}'.format(dict.setdefault('telefone', None)))
print(dict)