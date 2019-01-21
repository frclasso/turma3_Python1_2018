#!/usr/bin/env python3

a = 5

def muda_valor():
    global a  # altera a valor original global
    a = 7
    print(f"'a' dentro da funcao:{a}")
    return

# chamando a funcao
muda_valor()

# fora da funcao
print(f"Fora da funcao:{a}")