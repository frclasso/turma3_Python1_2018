#!usr/bin/env python3


import urllib.request

try:
    my_url = input('Digite uma url: ')
    page = urllib.request.urlopen(my_url)

    arquivo_html = input('Digite o nome do arquivo: ')
    with open(arquivo_html, 'w') as file:
        for line in page:
            file.write(str(line, encoding='utf-8'))

except:
    print('Nao foi possivel encontrar a ulr solicitada')

print('Done..')



