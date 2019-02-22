#!/usr/bin/env python3


def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError("Ao menos um argumento deve ser inserido")
    elif numargs == 1:
        start = 0
        stop = args[0]
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("inclusive_range espera 3 argumentos, "
                        "recebeu:{}".format(numargs))

    i = start
    while i <= stop:
        yield i
        i += step


for i in inclusive_range(20):
    print(i, end=', ')