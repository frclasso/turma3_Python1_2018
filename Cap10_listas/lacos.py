#!/usr/bin/env python3


cars = [
    [['Audi', 'BMW', 'Porsche'],
     ['Mercedez', 'Chrysler']
     ],
    [
        ['Ferrari', 'Lamborghini', 'Fiat'],
        ['Buggati']
    ],
    [
        ['Jeep', 'Buick', 'Lexus'],
        ['Bentley', 'Ford', 'Chevy']
    ]


]

# for linha in cars:
#     for car in linha:
#         print(car)

# for linha in cars:
#     for c in linha:
#         for k, car in enumerate(c):
#             print(k,car)

for linha in cars:
    for c in linha:
        for car in c[0].split():
            print(car, end=', ')
