#!/usr/bin/env python3


# ValueError, IOError

def main():
    try:
        for line in readfile('testefile.txt'):
            print(line.strip())
    except IOError as e:
        print('Nao foi possivel ler o arquivo', e)
    except ValueError as e:
        print("Nome errado", e)


def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError("O nome do arquivo precisar "
                         "terminar em .txt")


if __name__=="__main__":
    main()