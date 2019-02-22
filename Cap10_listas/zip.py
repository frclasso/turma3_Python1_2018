#!/usr/bin/env python3

questions = ['name', 'questions', 'favorite color']
answers = ['Lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print("What''Go', 'Django',s your {}? It's {}.".format(q, a))