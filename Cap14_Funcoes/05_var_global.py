#!/usr/bin/env python3

def calcula_tempo(distancia, velocidade):
    tempo = distancia/velocidade
    velocidade = 0
    return tempo

def calcula_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia

v = 100  # global

t = calcula_tempo(10, 5)
print(v)
print(t)

d = calcula_distancia(v, t)  # reuso
print(d)