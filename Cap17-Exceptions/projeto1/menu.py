#!/usr/bin/env python3

from salvaDados import *
#from salvaDados import salvar
from deletaCadastro import deleta_cadastro
from atualizaCadastro import *
from cadastro import cadastro_clientes

def lista_clientes(): # dentro de clientes.csv
    try:
        with open('clientes.txt', 'r') as file:
            for line in file:
                print(line, end='')

    except IOError: print('Arquivo nao encontrado')
    opcao()


clientes = []  # salva os dados cadastrados temporariamente



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
        print()
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

