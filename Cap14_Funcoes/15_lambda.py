#!/usr/bin/env python3


# funcoes anonimas - lambdas

minha_soma = lambda x,y:x+y

# print(minha_soma(20,30))
# print(minha_soma(220,30))
# print(minha_soma(2000,30))


# def calcula_tempo(distancia, velocidade):
#     tempo = distancia/velocidade
#     velocidade = 0
#     return tempo
#
# def calcula_distancia(velocidade, tempo):
#     distancia = velocidade * tempo
#     return distancia

calculatempo = lambda distancia, velocidade:distancia/velocidade

tempo = calculatempo(100,20)
print(tempo)


calculadistancia = lambda velocidade,tempo:velocidade * tempo
print(calculadistancia(100,tempo))
