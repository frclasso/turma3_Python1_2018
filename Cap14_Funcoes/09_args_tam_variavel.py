#!/usr/bin/env python3

def info(x,y, *args):
    """This prints a variable passed arguments"""
    print('Valor de x: ', x)
    print('Valor de y: ', y)
    print('Valor de args', args)
    # for var in args:
    #     print(f'O valor de args:', var)

# chamando a funcao
#info(10)
info(20, 30, 40, 50, 60)