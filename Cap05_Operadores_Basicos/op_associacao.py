# in e not in

pessoas = ['Fabio', 'Joao', 'Sandro', 'Douglas', 'Guilherme', 'Marcelo',
           'Marcelo Caon', 'Mauricio']

print('Mauricio' in pessoas) # True
print('Jessica' in pessoas) # False
print('Jessica ' not in pessoas) # True

# if => se

if 'Fabio' in pessoas or 'Jessica' in pessoas:
    print('OK')
