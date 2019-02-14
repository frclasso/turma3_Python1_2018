#!/usr/bin/env python3

# Exceçao generica UnknowError


import sys

def main():
    try:
        x = 5/0
    except ZeroDivisionError: # ValueError
        print('Erro, nao é possivel dividir por zero')
    except:
        print(f'UnknowError:{sys.exc_info()[0]}') #Erro desconhecido
    else:
        print('OK!!')
        print(x)

main()