#!/usr/bin/env python3

secret = 'swordfish'
pw =''
auth = False # autorizado, iniciado com valor False
count = 0 # contador de tentativas
max_attempt = 5 # numero maximo de tentativas

while pw != secret:
    count += 1
    if count > max_attempt:break
    pw = input("{}:What's the secret word?".format(count))
else:
    auth = True
print('Authorized' if auth else 'Calling the FBI')