
#!/usr/bin/env python3

total = 0  # variavel global

def sum(arg1, arg2):
    total = arg1 + arg2  # variavel local
    print('Dentro da funcao o valor de total é: ', total)
    return

# chamando a funcao
sum(10, 20)
print()
print('Fora da funcao o valor de total é: ', total)