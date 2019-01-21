#!/usr/bin/env python3

# Passagem por referencia, quando vc altera a variável original


def change_me(mylist):
    """This changes a passed list into this function"""
    print('Values inside the function BEFORE change: ', mylist)
    mylist[2] = 50
    print('Values inside the function AFTER change: ', mylist)

mylist = [10, 20, 30]

# chamando a funcao
change_me(mylist)

print(mylist)