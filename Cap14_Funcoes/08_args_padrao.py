#!/usr/bin/env python3

def info(nome, idade, linguagem='Python'):
    """Imprime informacoes de usuario passadas como argumento"""
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Linguagem favorita: ', linguagem)

print(info('Fabio', 44, 'Julia'))