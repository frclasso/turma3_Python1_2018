#!/usr/bin/env python3


import time


def processo():
    time.sleep(2) # 2 segundos


# medir o tempo de execucao do processo
t0 = time.clock()

processo()
print(time.clock() - t0, 'Segundos iniciais')

# medindo todo o tempo
t0 = time.time()
processo()
print(time.time() - t0, 'Segundos totais')

# time.perf_counter or time.process_time