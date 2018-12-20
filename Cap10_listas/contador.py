

myList = ['Python', 'Go', 'Django', 'PHP', 'C', 'C++', 'Java',
          'JavaScript', 'Julia Lang', 'Unix', 'Shell',
          'Bash','Python', 'Go', 'Django', 'PHP', 'C', 'C++', 'Java',
          'JavaScript', 'Julia Lang','Python', 'Go', 'Django', 'PHP', 'C', 'C++', 'Java',
          'JavaScript', 'Julia Lang','Python', 'Go', 'Django', 'PHP', 'C', 'C++', 'Java',
          'JavaScript', 'Julia Lang','Python', 'Go', 'Django', 'PHP', 'C', 'C++', 'Java',
          'JavaScript', 'Julia Lang','Julia Lang', 'Unix', 'Shell',
          'Julia Lang', 'Unix', 'Shell','Julia Lang', 'Unix', 'Shell',
          'Go', 'Django','Go', 'Django','Go', 'Django','Go', 'Django'
          ]

count = 0
for c in myList:
    if c == 'Python':
        count += 1
print(count)

# usando a funcao count()
print(myList.count('Python'))
