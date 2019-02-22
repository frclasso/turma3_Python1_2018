#!/usr/bin/env python3

clientes = {} # chave : valor
print(type(clientes))

usuarios = {'Id': None, 'Nome': None, 'Função': None}


print(usuarios.items())
print(usuarios.keys())
print(usuarios.values())

for k,v in usuarios.items():
    print(k,v)

usuarios.update({'Nome':'Fabio'})
usuarios['Id'] = 12334
print(usuarios)

print(usuarios['Nome'])

pessoa = {'Nome': 'Joana', 'idade':38}
#del pessoa['Nome']
pessoa.clear()
print(pessoa)

