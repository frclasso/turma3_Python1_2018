#!/usr/bin/env python3

import datetime

def main():
    now = datetime.datetime.now()
    print(now)
    print(f"{now.year}/{now.month}/{now.day}")
    print(f'Hora local:{now.hour}:{now.minute}:{now.second}')



if __name__=="__main__":
    main()