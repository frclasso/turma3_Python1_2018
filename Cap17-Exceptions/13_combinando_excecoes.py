#!/usr/bin/env python3

# ZeroDivision, ValueError

# try:
#     a = int(input('Digite o primeiro numero:'))
#     b = int(input('Digite o segundo numero:'))
#     print("{} '/' {} '=' {}".format(a,b,a/b))
# except (ZeroDivisionError,ValueError) as e:
#     print('Erro:', e)

try:
    a = int(input('Digite o primeiro numero:'))
    b = int(input('Digite o segundo numero:'))
    print("{} '/' {} '=' {}".format(a,b,a/b))
except ZeroDivisionError:
    print('Denominador nao pode ser zero')
except ValueError: # tetar com TypeError
    print('a e b precisam ser do tipo inteiro')
except Exception as e:
    print("Erro desconhecido", e)
    raise