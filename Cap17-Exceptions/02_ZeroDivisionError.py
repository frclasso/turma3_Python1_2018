#!/usr/bin/env python3


# ZeroDivisionError
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('Denominador nao pode ser zero')
#


def div_42_por(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print('Erro: Denominador nao pode ser zero')

print(div_42_por(0))