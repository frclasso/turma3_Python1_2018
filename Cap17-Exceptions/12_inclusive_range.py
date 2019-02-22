#!/usr/bin/env python3

# inclusive range - simula range(start, stop, step)

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step =1

    # inicializando paramentros
    if numargs < 1:
        raise TypeError(f'Esperado ao menos um argumento, recebido',numargs)
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Esperado 3 argumentos, recebido', numargs)

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


def main():
    try:
        for i in inclusive_range(1, 20, 5, 4):
            print(i, end=' ')
    except TypeError as e:
        print(f'Erro de range:', e)


if __name__=="__main__":main()