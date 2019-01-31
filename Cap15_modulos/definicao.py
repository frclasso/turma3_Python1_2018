#!/usr/bin/env python3

# from MODULO import funcao,var, classe
from origem import somaNum, power

print(somaNum(4,3))
print(power(3,4))

import origem as o
print(o.somaNum(3,4))

from origem import *
print(somaNum(3,4))