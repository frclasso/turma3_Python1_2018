#!/usr/bin/env python3

# Passagem por referencia, quando vc altera a variável original


def change_me(x):
    """This changes a passed list into this function"""
    print('Values inside the function BEFORE change: ', mylist)
    mylist[2] = x
    print('Values inside the function AFTER change: ', mylist)

mylist = [10, 20, 30]

# chamando a funcao
change_me(50)

print(mylist)