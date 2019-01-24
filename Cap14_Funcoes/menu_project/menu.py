#!/usr/bin/env python3


print('Cadastro  de clientes')
print()


def cadastro_clientes():
    nome = input('Digite nome do usuario: ')
    idade = input('Didige a idade: ')
    sexo = input('Digite o sexo: ')
    clientes.append(nome)
    clientes.append(idade)
    clientes.append(sexo)


def atualiza_cadastro(): # dentro de clientes.csv
    print('Alterar cadastro')


def deleta_cadastro(): # dentro de clientes.csv
    print('Deletar cadastro')


def lista_clientes(): # dentro de clientes.csv
    print('Lista de clientes:', clientes)


# def salvar():
#     # Salvando em um arquivo .csv
#     import csv
#     with open('clientes.csv', 'w') as clientes_file:
#         for c in clientes:
#             clientes_write = csv.writer(clientes_file)
#             clientes_write.writerow(c)
#             clientes_write.writerow('\n')
#         print('Dados salvos com sucesso')


clientes = []  # salva os dados cadastrados temporariamente

def salvar():
    fh = open('clientes.txt', 'a')
    for c in clientes:
        fh.write(c[0] + ',')
        fh.write(c[1]+',')




def opcao():
    while True:
        print()
        menu = int(input('''Escolha uma opção
                    1 para cadastrar novo cliente;
                    2 para alterar cadastro existente;
                    3 para Deletar cadastro;
                    4 para listar os clientes cadastrados
                    5 para gravar dados
                    0 para Sair do programa: '''))
        if menu == 0:
            break
        if menu == 1:
            cadastro_clientes()
        elif menu == 2:
            atualiza_cadastro()
        elif menu == 3:
            deleta_cadastro()
        elif menu == 4:
            lista_clientes()
        elif menu == 5:
            salvar()
        else:
            print('Voce deve escolher uma opção')

print()

# chamada de funcao
opcao()

