

# variavel de pesquisa

def atualiza_cadastro():
    try:
        with open('clientes.txt', 'a') as file:
            for dados in file:
                file.readlines()
    except IOError:
        print('Arquivo nao encontrado')

    print('Alterar cadastro')