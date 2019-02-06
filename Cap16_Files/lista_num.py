

file=open('numeros.txt','w')
for x in range(0,150):
    file.write(str(x)+' ')
file.close()

print("Done...")