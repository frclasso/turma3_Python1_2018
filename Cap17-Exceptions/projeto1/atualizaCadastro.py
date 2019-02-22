

def atualiza_cadastro():
    try:
        fh = open('clientes.txt', 'r')
        clientes = []

        for line in fh.readlines():
            clientes.append(line)

        for n, cliente in enumerate(clientes):
            print(n, cliente,end='')
        #print(clientes[0])
        fh.close()
    except FileNotFoundError:
        print('Arquivo não encontrado')
        print()

atualiza_cadastro()
