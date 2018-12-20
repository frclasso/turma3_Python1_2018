#!/usr/bin/env python3

telefones = {
    'Fabio':'9999-8888',
    'Juliana':'9999-9876',
    'Giovanna':'99887-4546',
    'Erick':'9987-3455'
}

#print(sorted(telefones.keys()))

for k, v in enumerate(sorted((telefones.keys()))):
    print(k,v)
print()

dict = {'Name':'Zara'}
print(dict.setdefault('Age',16))
print(dict.setdefault('Sex',None))
print(dict)

dict2 = {'ID':1234}

dict.update(dict2)
print(dict)

print('Fabio' in telefones)
print('9999-8888' in telefones)
print('9999-8888' in telefones.values())
