#!/usr/bin/env python3

# valores aleatorios
# random
import random

elementos = ['ar', 'terra', 'agua', 'fogo']
str = 'Python'
num = [1,2,3,4,5,6,7]


# choice(seq)
print(random.choice(elementos))
print(random.choice(str))
print(random.choices(str))



# random.randrange()
print(list(range(1,102, 5)))
print(random.randrange(1, 102, 5))


# random.random()
print(random.random())

# seed()
#random.seed(3)
print(random.random())

#shuffle
random.shuffle(elementos)
print(elementos)

# uniform()
print(random.uniform(5,10))
print(int(random.uniform(5,10)))
print(random.uniform(7,14))
print()

import math
print(math.pi)
print(math.e)

# sample
megaSena = random.sample(range(1, 61),6)
print('Mega sena:', megaSena)
print(sorted(megaSena))
print()

import itertools

colors = ['vermelho', 'azul', 'roxo', 'amarelo','lilas']

# combinations, ordem nao importa
contador = 0
for c in itertools.combinations(colors, 3):
    contador += 1
    print(c)
print()

# permutations, ordem importa
election = {1:'Bolsonaro', 2:'Haddad', 3:'Ciro', 4:'Eymael', 5:'Daciolo'}
for k, p in enumerate(itertools.permutations(election),start=1):
    print(k, p)

