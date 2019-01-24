#!/usr/bin/env python3

# Fibonacci

def fibo(n):
    result = []
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a + b
    print()

fibo(6)

# def fibo2(n):
# #     result = []
# #     a,b = 0,1
# #     while a < n:
# #         result.append(a)
# #         a,b = b, a + b
# #     return result
# #
# #
# # x =fibo2(6)
# #
# # print(x)