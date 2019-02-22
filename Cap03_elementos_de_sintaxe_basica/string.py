
texto = "Hello World"

#print(texto)
# indice, iniciam por zero
# print(texto[0])
# print(texto[1])
# print(texto[6])
# print(texto[-1])
# print(texto[-2])

# Fatias / Slices [:]
# print(texto[:])
# print(texto[6:])
# print(texto[:5])

# concatenar +
linguagem  = "Python 3"

print(texto + linguagem)
print(texto + ' ' + linguagem)
print(texto[:5] + ' ' + linguagem)

novotexto = texto[:5] + ' ' + linguagem
print(novotexto)

print(texto[::-1])
