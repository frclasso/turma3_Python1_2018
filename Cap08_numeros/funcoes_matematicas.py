#!/usr/bin/env python3


print('abs -45:', abs(-45))

# potencia
print('potencia entre, 3 ** 2:', 3 ** 2)

import math

print('abs -45:', math.fabs(-45)) # float abs
print()
# ceil e floor
print('Math ceil 45.17:', math.ceil(45.17))
print('Math ceil -45.17:', math.ceil(-45.17))
print('Math ceil 100.2:', math.ceil(100.2))
print('Math ceil 100.72:', math.ceil(100.72))
print()

print('Math floor 45.17:', math.floor(45.17))
print('Math floor -45.17:', math.floor(-45.17))
print('Math floor 100.2:', math.floor(100.2))
print('Math floor 100.72:', math.floor(100.72))
print()

print('Potencia pow(x,y):', pow(3,2))
print('Exponencial exp(x)', math.exp(3))
print()

print("PI:", math.pi)
print('Math Log 100.2:', math.log(100.2))
print('Math Log 100.72:', math.log(100.72))
print('Math Log PI:', math.log(math.pi))
print()

print('Math log(10) 100.2:', math.log10(100.2))
print('Math log(10) 100.72:', math.log10(100.72))
print('Math log(10) PI:', math.log10(math.pi))
print()

#acos, cos, arcoseno, arcotangente
print('acos de 0.64:', math.acos(0.64))
print('cosseno de 0:', math.cos(0))
print('Cosseno de uma volta:',math.cos(2 * math.pi))
print('asin de -1:', math.asin(-1))
print('atan de 1:', math.atan(1))
print()
# hipotenusa, radianos
print('Hypotenusa(3,2):', math.hypot(3,2))
print('Radianos:', math.radians(3))
print('Radianos:', math.radians(-3))
print('Radianos:', math.radians(0))
print('Degrees:', math.degrees(0.05235987755982989))

