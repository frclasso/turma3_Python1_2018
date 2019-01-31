#!/usr/bin/env python3

import sys

def main():
    # print("Python version {}.{}.{}".format(*sys.version_info))
    # print(f'Plataforma:{sys.platform}')
    # print()
    #
    #
    # # funcoes do sistema operacional
    # import os
    # print(f'Nome do OS:{os.name}')
    # print(f"Path:{os.getenv('PATH')}")
    # print(f'Diretorio atual:{os.getcwd()}')
    # print()


    # Trabalahndo com url's
    import urllib.request
    page = urllib.request.urlopen('https://docs.python.org/')

    print(page)
    for line in page:
        print(str(line, encoding='utf=8'), end=' ')

if __name__ =="__main__":
    main()