#!/usar/bin/env python

# Renomeando vários arquivos
import os

os.chdir('/Users/fabio/Desktop/turma3_Python1_2018/Cap16_Files/imgs')

#print(os.getcwd())

# ler os arquivos
for f in os.listdir():
    #print(f)
    #print(os.path.splitext(f))
    file_name, file_extension = os.path.splitext(f)
    #print(file_name.split('-'))
    f_nome, f_titulo, f_num = file_name.split('-')
    #print(f_nome)

    f_nome = f_nome.strip()
    f_titulo = f_titulo.strip()
    f_num = f_num.strip()[1:].zfill(2)

    #renomear e salvar
    novo_nome ='{}-{}{}'.format(f_num,f_nome, file_extension)
    os.rename(f, novo_nome)
