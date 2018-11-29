#!/usr/bin/env python3

# ex 01
# for letter in 'Python':
#     if letter == 'h':
#         break
#     print('Current letter:', letter)


# ex 2

n = int(input('Any number: '))

numbers = [11,33,44,55,75,37,21,34,41,32]
for num in numbers:
    if num == n:
        print('Number found in list')
        break
else:print('Number not found in list...')

