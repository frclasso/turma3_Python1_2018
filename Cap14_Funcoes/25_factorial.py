#!/usr/bin/env python3

# Factorial

num = int(input('Digite um número: '))
factorial = 1

if num < 0:
    print("Não existe fatorial de números negativos.")
elif num == 0:
    print('Fatorial de 0 é 1.')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"Factorial de {num} é {factorial}")


"""
Definicao:

Fatorial é um número natural inteiro positivo, o qual é representado por n!

O fatorial de um número é calculado pela multiplicação desse número por todos os 
seus antecessores até chegar ao número 1. Note que nesses produtos,
 o zero (0) é excluído.

O fatorial é representado por:

n! = n . (n – 1) . (n – 2) . (n – 3)!

Exemplo:

Fatorial de 6: 6! (lê-se 6 fatorial)

6! = 6 . 5 . 4 . 3 . 2 . 1 = 720
"""