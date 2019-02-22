#!/usr/bin/env python3

# acumuladores

whishList = []

while True:
    coisas = input('Digite um nome de algo que voce goste ou 0 para sair:')
    if coisas == '0':
        break
    else:
        whishList.append(coisas) # adiciona
        print('Item adicionado com sucesso')
print()
print(f'Sua lista de desejos:{whishList}')
print(f'Quantidade de items:{len(whishList)}') # length