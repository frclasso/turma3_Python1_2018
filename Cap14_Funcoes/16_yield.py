#!/usr/bin/env python3


# yield - funcoes geradoras

def get_generator():
    for i in range(10):
        yield i


for number in get_generator():
    print(number, end=',')

print()


def get_list():
    numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers


for number in get_list():
    print(number, end=',')