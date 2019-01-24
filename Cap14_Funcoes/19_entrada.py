#!/usr/bin/env python3


def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print(f'Digite um valor entre {maximo} e {minimo}')
        except:
            print(f'Voce deve digitar um numero inteiro...')


x = valida_inteiro('Hello ', 5, 10)
print(x**2)
