#!/usr/bin/env python3

# dicionarios


# chaves => int ou string
# valor => qq tipo python

dict = {} # cria um dicionario vazio

dict2 = {'Nome':'Fabio', 'idade':43, 'tel':99998888}
# Acessar os valores
print(dict2['Nome'])
print('Imprimir idade:',dict2['idade'])
print(dict2['tel'])


funcionarios = {'Fabio':['classo', 43, 'Masc'],
                'Joao':['Cavichiolli', 33, 'Masc']}
print(funcionarios['Fabio'])
print(funcionarios['Joao'])

print(dict2.keys())
print(dict2.values())
print(dict2.items())

for x,y in dict2.items():
    print(x,'=>', y)


print('Fabio' in funcionarios)
print('Fabio' in dict2.values())