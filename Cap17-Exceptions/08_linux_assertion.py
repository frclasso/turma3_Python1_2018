#!/usr/bin/env python3


import sys


def linux_interaction():
    assert ('Linux' in sys.platform), 'Function can only run ' \
                                       'on Linux Systems'
    print('Doing something')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')
else:
    print("Executing else clause")


