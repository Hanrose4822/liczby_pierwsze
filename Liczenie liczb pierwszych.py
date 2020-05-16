import time
from datetime import datetime


lp = []
liczba = 1
t1 = time.time()
while True:
    liczba = liczba + 1
    for x in range(2, liczba+1):
        if liczba % x == 0:
            break
    
    if x == liczba:
        t2 = time.time()
        lp.append(x)
        print('liczba pierwsza', x)
        print(f'\t {t2-t1:.2f}')
        t1 = t2

