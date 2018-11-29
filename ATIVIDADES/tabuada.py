"""Criar um aplicacao de tabuada simples,
imaginem ensinar tabuada pra uma criança"""


# print(n * 0)
# print(n * 1)
# print(n * 2)
# print(n * 3)
# print(n * 4)
# print(n * 5)
# print(n * 6)
# print(n * 7)
# print(n * 8 )
# print(n * 9 )
# print(n * 10 )

print('Ola amiguinho')
n = int(input('Digite a tabuada que vc quer aprender:'))


# dicas
# for,

# numeros = [0,1,2,3,4,5,6,7,8,9,10]
# for num in numeros:
#     print(f'O Numero {n} * {num} = {num * n}')

# range
numeros = range(11)
for num in numeros:
     print(f'O Numero {n} * {num} = {num * n}')


