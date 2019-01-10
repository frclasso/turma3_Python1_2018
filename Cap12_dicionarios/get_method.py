#!/usr/bin/env python3

telefones = {
    'Fabio':'9999-8888',
    'Juliana':'9999-9876',
    'Giovanna':'99887-4546',
    'Erick':'9987-3455'
}

outrosNums = {'Pedro':'8889-44433',
              'Amanda':'9998-8877'}

# print(telefones.get('Fabio'))
# print(telefones.get('Ana'))
#print(telefones['Ana'])


# items() retorna um dicionario com par chave/valor
# print(telefones.items())
# # keys() retorna um dicionarios com as chaves dos dicionarios
# print(telefones.keys())
# # values() retorna um dicionario com os valores
# print(telefones.values())
#
# print(list(telefones.keys()))
# print(list(telefones.values()))

# deletando items

# pop
# telefones.pop('Fabio')
# print(telefones)
# # del
# telefones.__delitem__('Juliana') # na apostila del
# print(telefones)
# # popitem
# telefones.popitem() # deleta o ultimo, não aceita passar parametros
# print(telefones)


# update
telefones.update(outrosNums)
print(telefones)

# sorted - ordena
print(sorted(telefones))
for k, x in enumerate(sorted(telefones),start=1):
    print(k, x)