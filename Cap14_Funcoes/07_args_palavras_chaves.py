#!/usr/bin/env python3

def info(nome, idade):
    """Imprime informacoes de usuario passadas como argumento"""
    print('Nome: ', nome)
    print('Idade: ', idade)

# chamando
#info(44, 'Fabio')


info(idade=38, nome='Juliana')  # argumentos de palavra chave,
                                # nao importa a ordem
