#!/usr/bin/env python3

import time

localtime = time.localtime(time.time())
#print('Hora local:', localtime)

# asctime
othertime = time.asctime(time.localtime(time.time()))
print('asctime:', othertime) # Wed Jan  9 20:21:51 2019