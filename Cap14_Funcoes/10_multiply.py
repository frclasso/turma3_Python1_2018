#1/usr/bin/env python3


def multiply(*args):
    z = 1
    for num in args:
        z *= num  # z = z * num
    return z

print(multiply(4,5))
print(multiply(4,5, 6))
print(multiply(4,5, 6, 7))
print(multiply(4,5, 6,7,8))