from cadastro import clientes

def salvar():
    try:
        with open('clientes.txt', 'a') as file:
            for nome in clientes:
                file.write(nome + ',')
                file.write('\n')
    except IOError:
        print('Arquivo nao encontrado')
