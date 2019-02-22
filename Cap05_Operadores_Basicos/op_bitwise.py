a, b = 60, 13
d = 60
print(format(~d, '08b'))
c = ~a
print('Negacao de a: ',c, '==>', format(c, '08b'))

print()

print('a=', a,'==>', format(a, '08b'))
print('b=', b,'==>', format(b, '08b'))
print()
c = ~a
print('Negacao de a: ',c, '==>', format(c, '08b'))
print()
print()
c = 0
c = a & b
print('a AND b =>', c,'==>', format(c, '08b'))
print()

c = a | b
print('a OR b =>', c, '==>', format(c, '08b'))
print()

c = a ^ b
print('a XOR b =>', c, '==>', format(c,'08b'))
print()

c = ~a
print('Negacao de a: ',c, '==>', format(c, '08b'))
print()

c = a <<2
print(' a << 2: ', c, '==>', format(c, '08b'))
print()
c = a >> 2
print(' a >> 2: ', c, '==>', format(c, '0b'))

