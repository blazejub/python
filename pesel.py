PESEL = (input('Podaj pesel: '))
if (int(PESEL[9]) % 2 == 1):
    print('M')
elif (int(PESEL[9]) % 2 == 0):
    print('K')    
else: 
    print('Błąd')