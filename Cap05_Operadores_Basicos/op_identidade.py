# is , is not

x = [1,2,3]
y = [1,2,3]
z = x

print(x is y)
print(z is x)
print(z is not y)
print(y is x)

print(id(x))
print(id(y))
print(id(z))