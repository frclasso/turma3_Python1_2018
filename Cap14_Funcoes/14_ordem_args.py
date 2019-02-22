#!/usr/bin/env python3


def info(nome, idade,*args, linguagem='Python', **kwargs):
    """Imprime informacoes de usuario passadas como argumento"""
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Linguagem favorita: ', linguagem)
    print('args', args)
    print('kwargs', kwargs)

info('Fabio', 44, 20,30,50, carro='Audi')


# ordem - posicionais, *args, palavra-chave - **kwargs
