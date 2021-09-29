pkt = int(input('Podaj liczbę zdobytych punktów klasy: '))
f = float(input('Podaj frekwencję klasy: '))
so = float(input('Podaj srednia ocen klasy: '))

if (f >= 94 and so >= 4):
    pkt += 20
    print('Aktualna liczba punktow wynosi: ',pkt,'punktów')
else:
    print('Aktualna liczba wynosi: ',pkt, 'punktów ')

