
#!/usr/bin/env python

# Calculando datas futuras

from datetime import datetime, timedelta
now = datetime.now()

daquiDoisdias = now + timedelta(days=2)
print(f'Daqui dois dias será: {daquiDoisdias.date()}')
#print(daquiDoisdias)

tresSemanaasAtras = now - timedelta(weeks=3)
print(f'Tres semanas atrás: {tresSemanaasAtras.day}/'
      f'{tresSemanaasAtras.month}/'
      f'{tresSemanaasAtras.year}')
#print(tresSemanaasAtras)


