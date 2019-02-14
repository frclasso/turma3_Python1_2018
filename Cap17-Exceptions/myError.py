#!/usr/env python3


# Classe Error

class Error(Exception):
    '''Classe base para outras excecoes'''
    pass


class ValueTooSmallError(Error): # Herda de class Error
    """Levanta uma exceção quando o valor  de entrada
    é pequeno demais."""
    pass


class ValueTooLargeError(Error):# Herda de class Error
    """Levanta uma exceção quando o valor  de entrada
    é grande demais."""
    pass

# advinhe o numero...
number = 5

while True:
    try:
        i_num = int(input('Digite um numero: '))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('Esse valor é muito pequeno, tente novamente')
        print()
    except ValueTooLargeError:
        print("Esse valor é muito grande, tente novamente")
print('Parabens vc advinhou o numero')