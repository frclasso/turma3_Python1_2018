#!/usr/bin/env python3

# **kwargs

def people(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('O povo de {} diz: {}.'.format(k, kwargs[k]))
    else:print('Sem parametros')


def main():
    x = dict(SC='Greve', SP="Paralisacao", RJ='Corrupcao',
             PR='Lava-jato')
    people(**x)

    # people(SC='Greve', SP="Paralisacao", RJ='Corrupcao',
    #        PR='Lava-jato')



if __name__ == '__main__':
    main()

