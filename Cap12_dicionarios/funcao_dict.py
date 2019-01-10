#!/usr/bin/env python3

# função dict([])  - recebe tuplas, o primeiro item é a chave

myDict = dict([('nome', 'Fabio'), ('idade', 44)])
print(myDict)


# copiando dicionario
outroDict = myDict.copy()
print(outroDict)

print(id(myDict))
print(id(outroDict))

myDict['Tel']='99998888'
print(myDict)

myDict.update({'email': 'fabio@gmail.com'})
print(myDict)

myDict.setdefault('Endereco', None)
print(myDict)

