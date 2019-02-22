#!/usr/bin/env python3

# contadores

""" a variável contador é iniciada com valor zero, novos
valores serão adicionados através da instrução input e
serão incrementados contador += 1"""

contador = 0

while True:
    letras = input('Digite uma letra, ou esc para sair:')
    if letras == 'esc':
        break
    else:
        print('Letra adicionada')
        contador += 1
print('Quantidade de letras adicionadas:{}'.format(contador))
#print(f'Quantidade de letras adicionadas:{contador}')
#print(f'Quantidade de letras adicionadas:', contador) # Python 2