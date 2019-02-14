#/usr/bin/env python3

def temp_converter(var):
    try:
        return int(var)
    except ValueError as Argument:
        print('Valor do argumento incorreto', Argument)


temp_converter()