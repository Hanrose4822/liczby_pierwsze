import time



lp = []
szukana_liczba = 1
t1 = time.time()


def czy_liczba_pierwsza(liczba):
    if type(liczba) != int:
        return False
    if liczba <= 1:
        return False
    for x in range(2, liczba + 1):
        if liczba % x == 0:
            break

    if x == liczba:
        return True

    return False


while True:
    szukana_liczba = szukana_liczba + 1

    if czy_liczba_pierwsza(szukana_liczba):
        t2 = time.time()
        lp.append(szukana_liczba)
        print('liczba pierwsza', szukana_liczba)
        print(f'\t czas wyszukiwania liczby: {t2-t1:.2f}')
        t1 = t2
