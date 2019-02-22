#!/usr/bin/env python3


# gerador

def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step


for i in inclusive_range(0, 25, 5):
    print(i, end=', ')


print(list(range(0, 25)))