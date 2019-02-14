#!/usr/env python3

import csv

print('Cadastro  de clientes')
print()

clientes =[]

def cadastro_clientes():
    try:
        nome = input('Digite nome do usuario: ')
        sobrenome = input('Didige o sobrenome: ')
        email = input('Digite o email: ')
        clientes.append(nome)
        clientes.append(sobrenome)
        clientes.append(email)

        with open('clientes.txt', 'a') as file:
            for nome in clientes:
                file.write(nome +',')
            file.write('\n')
    except FileNotFoundError:
        print('Arquivo  nao encontrado')


#cadastro_clientes()
