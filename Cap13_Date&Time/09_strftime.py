#!/usr/bin/env python3


# Formantando a saída datetime.strftime()

"""Formatando dias:
    %a => abrevia dias da semana: Mon, Tue, Wed
    %A => nome completo dos dias: Monday, Tuesday, Wednesday
    %d => dia do mês em formato numerico
"""
"""Formatando meses
    %b => abrevia meses: Jan, Feb,
    %B => nome completo dos meses: Janeiro,Fevereiro
    %m => meses em formato numerico
"""

"""Formantando horas
    %H => horas
    %M => minutos
    %S => segundos
    %p => AM ou PM
"""

"""Formantando anos
    %y => dois algarismos: 19
    %Y => quatros algarismos:2019
"""

import time

t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
t =time.mktime(t)
print(time.strftime("%B %d %Y %H:%M:%S", time.localtime(t)))