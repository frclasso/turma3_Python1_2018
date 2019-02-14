#!/usr/bin/env python3


# FileNotFoundError

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as e: # capturar erro
    print('Erro, arquivo nao encontrado', e)