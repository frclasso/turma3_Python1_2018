#!/usr/bin/env python3


# rolodex

rolodex = {
    'Aaron':5556069,
    'Bill':5559842,
    'David':5552603,
    'Dillon':5555432,
    'Barbara':5559874,
    'Jim':5550998,
    'Mother':55523656,
    'Father':555997756,
    'Olivia':5558765,
    'Giovanna':5550909,
    'Erick':5550808,
}

# inserindo novo cadastro
rolodex['Amanda'] = 55598763
#print(rolodex)

rolodex.update({'Fabio':5554411})  # update tem usar chaves
#print(rolodex)

rolodex['David'] = 5552603, 5556060

# definindo uma funcao para acessar os valores


def caller_id(numeroProcurado):
    for name, num in rolodex.items():
        if num == numeroProcurado:
            return name


#print(rolodex['David'])
#print(caller_id((5552603, 5556060)))

rolodex['Angela'] = 555544332

def newCaller():
    nome = input('Nome')
    telefone = input('telefone')
    rolodex.update({nome:telefone})
    return rolodex

newCaller()

with open('rolodex.txt', 'w') as f:
    for nome, telefone in rolodex.items():
        f.write(nome+'==> ')
        f.write(str(telefone))
        f.write('\n')

print('Done...')
