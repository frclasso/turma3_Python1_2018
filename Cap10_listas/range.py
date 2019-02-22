


listaNumeros = list(range(1, 100, 5))

print(listaNumeros)
print(len(listaNumeros))
print(min(listaNumeros))
print(max(listaNumeros))
print()

# membros in e not in
cavaleiros = ['fome', 'peste', 'guerra', 'morte']
print('peste' in cavaleiros)
print('war' in cavaleiros)
print('war' not in cavaleiros)
print()
# lacos
for k, cavaleiro in enumerate(cavaleiros, start=1):
    print(k, cavaleiro)