

lista  = [9,9,9,8,7,1,2,3,4,5,6,7,8,9,10]

print(type(lista))
minhaTupla = tuple(lista)
print(minhaTupla)
meuSet = set(minhaTupla)
print(meuSet)

string = 'Python'
print(list(string))
print(tuple(string))

x = 10
y = str(x)
print(type(y))

print(x + x)
print(str(x) + y)
z = int(y)
print(x + z)