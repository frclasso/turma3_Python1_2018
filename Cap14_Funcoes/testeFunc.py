#!/usr/bin/env python3

# definindo uma funcao - def

# def my_func(parametros):
#     return parametros
#
# # chamada de funcao
# print(my_func('Argumentos'))

def Func(this, that, other, *args, **kwargs):
    print()
    print('This is a test function',
          kwargs['one'], kwargs['two'], kwargs['tree'],
          kwargs['four'], this, that, other, args
          )
    print()

Func(5,6,7,8,9,10, one=1, two=2, tree=3,four=4)
