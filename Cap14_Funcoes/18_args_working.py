#!/usr/bin/env python3

# definindo a função
def kitten(*args):
    if len(args):  # caso receba ao menos um argumento
        for s in args:
            print(s)
    else:
        print('Owwww No parameters!') # caso nao receba nenhum


# definindo uma variavel tupla
x = ('meow', 'gurr', 'purr', 'hello', 'world')

kitten() # chamando a funcao sem parametros
kitten(*x) # passando a variavel x como *args
