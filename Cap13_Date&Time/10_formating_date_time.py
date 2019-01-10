#!/usr/bin/env python3


from datetime import datetime

now = datetime.now()

# dias
print(now.strftime("%a, %A, %d"))
# meses
print(now.strftime("%b, %B, %m"))
# hora
print(now.strftime("%H:%M:%S %p"))
# ano
print(now.strftime("%y, %Y"))

# juntando tudo
print(f"Hoje são {now.strftime('%d')} de {now.strftime('%B')} ,"
      f"hora {now.strftime('%H:%M:%S %p')},"
      f" de {now.strftime('%Y')}.")
