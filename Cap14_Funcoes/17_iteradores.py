#!/usr/bin/env python3

# iteradores

import sys

lista = [1,2,3,4,5]

it = iter(lista)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#print(next(it)) #StopIteration

# for x in it:
#     print(x, end=',')
#
# evitar Stop Iteration
while True:
    try:
        print(next(it),end=', ')
    except StopIteration:
        sys.exit()