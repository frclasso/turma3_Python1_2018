#!/usr/bin/env python3

# if aninhado

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    if num % 3 == 0:
        print('Divisivel por 3 e por 2')
    else:
        print('Divisivel por 2 mas não por 3')
else:
    if num % 3 == 0:
        print('Divisivel por 3 mas não por 2')
    else:
        print('Nao é divisel por 3 nem por 2')