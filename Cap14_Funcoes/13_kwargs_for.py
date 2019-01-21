#!/usr/bin/env python3

def print_values(**kwargs):
    for key, value in kwargs.items():
        print('The value of {} is {}.'.format(key,value))

print_values(myname='Fabio',
             lang='Python',
             year=2019,
             city='Sao Jose',
             state='Santa Catarina',
             country='Brazil')