#!/usr/bin/env python3

amount = int(input('Enter amount: '))

if amount <= 1000:
    discount = amount * 0.05
    print(f'Discount:{discount}')
elif amount <= 5000:
    discount = amount * 0.10
    print(f'Discount:{discount}')
else:
    discount = amount * 0.15
    print(f'Discount:{discount}')

print(f'Net payable:{amount - discount}')
