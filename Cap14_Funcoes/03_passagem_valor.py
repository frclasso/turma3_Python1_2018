#!/usr/bin/env python3

# Passagem por valor

# Aqui o argumento esta sendo passado por valor e
# a referencia esta sendo sobrescrita dentro da funcao

def change_me(mylist):
    """This is change a passed list into this function"""
    mylist = [10,20,30]
    print("Values inside the function: ", mylist)
    return

# declarando a lista
mylist = [100,200,300]

# chamando a funcao
change_me(mylist)

print()
print("Values outside the function: ", mylist)