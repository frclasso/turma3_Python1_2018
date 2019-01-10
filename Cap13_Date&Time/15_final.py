#!/usr/bin/env python3

import os
import time
import sys
from datetime import datetime

def sleeping():
    x = 0
    while x < 5:
        print()
        print('Exibindo informacoes do Sistema opercional')
        v = sys.version_info
        print('Python version {}.{}.{}'.format(*v))

        w = (sys.platform).capitalize()
        print(f'Plataforma {w}')

        z = (os.name).capitalize()
        print(f'OS name: {z}')

        print("Proxima atualizacao em 3 segundos")
        time.sleep(3)
        x +=1

sleeping()
print()
print('***Programa sera encerrado automaticamente***')
now = datetime.now()
print()
print(f"Ultima atualizacao em: {now.date()} {now.hour}:{now.minute}")