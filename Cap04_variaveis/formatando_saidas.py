#!/usr/bin/env python3

# shebang - cabecalho

"""Formating strings - mode de imprimir variáveis"""

# variaveis
idade = 18 # inteiro
altura = 1.95 # real/numero de ponto flutuante
nome ='John' # string
sobreNome = 'Lennon'

# Python 2
# % - Place holder
# %d - inteiros
# %f - floats
# %s - strings

print('Usuario: Nome:%s, Sobrenome: %s, '
      'Altura: %.2f e Idade %d anos.' % (nome, sobreNome, altura,idade))


# Python 3.5.6 - 2017
# {} - place holder
# .format

print('Usuario: Nome: {}, Sobrenome: {}, '
      'Altura: {:.2f} e Idade {} anos.'.format(nome, sobreNome, altura,idade))


# Python 3.7 - 2018
# {} - place holder
# f

print(f'Usuario: Nome:{nome}, Sobrenome:{sobreNome}, '
      f'Altura:{altura}, Idade:{idade} anos')