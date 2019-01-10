#!/usr/bin/env python3

# localtime

import time

t = time.localtime()
#print(type(t))
print(t)
print(f'Ano:{t.tm_year}')
print(f'Mes:{t.tm_mon}')
print(f'Dia:{t.tm_mday}')
