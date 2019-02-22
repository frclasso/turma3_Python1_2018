
# listas

lista = ['abcd',7.86,2.22,'john',70.2]
outraLista = ['def', 'Maria']

# mutabilidade
lista[0] = 'ABCD'
print(lista)

# tuplas
tup1 = ('abcd',7.86,2.22,'john',70.2)
print(tup1[0]) # indice
print(tup1[2:]) # fatias
print(tup1[3] * 5) # repeticao
tup2 = 'def', 'Maria'
print(tup1 + tup2) # concatenacao


# Imutabilidade
#tup1[0] = 'ABCD'

tup3 = 'bola',  # parenteses opcional, a virgula nao
print(type(tup3))


print('Maria' in outraLista)