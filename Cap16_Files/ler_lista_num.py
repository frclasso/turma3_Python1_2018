

file=open('numeros.txt','r')
linhas=file.read()
num=''
for l in linhas:
    if l!=' ':
        num=num+l
    else:
        print(int(num),end=' ')
        num=''
    file.close()