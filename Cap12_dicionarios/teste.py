

usuarios = [
    '12345',{'Nome':'Fabio', 'Funcao':'Instrutor'},
    '22345',{'Nome':'Joana', 'Funcao':'Instrutor'},
    '32345',{'Nome':'Juliana', 'Funcao':'Instrutor'},
]


pessoa = {'1232425':['Fabio', 43, 'Florianopolis']}

# print(len(usuarios))
# print(str(usuarios[1]))


newUser = usuarios.copy()
otherUsers = usuarios
print(newUser)
print(otherUsers)
print(id(usuarios))
print(id(newUser))
print(id(otherUsers))

# fromkeys()

print({}.fromkeys([2,3]))
print()

users = {}.fromkeys(['Nome', 'Idade','Cidade'])
print(users)

