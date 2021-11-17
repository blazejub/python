def zadanie1():
    x = int(input("Podaj liczbę"))
    liczba = 0
    lista = [0,0,0,0,0]
    for i in range(5):
        liczba += x
        lista[i] += liczba
    print(lista)

def zadanie2():
    x = int(input("Podaj liczbę x"))
    y = int(input("Podaj liczbę y"))
    for i in range(x,y):
        if(i%2==0):
            print(i)
        
def zadanie3():
    x = int(input("Podaj liczbę x"))
    y = int(input("Podaj liczbę y"))
    lista = []
    for i in range(x,y):
        if(i % 2 != 0): 
            lista.append(i)
    lista.reverse()
    print(lista)

def zadanie4():
    lista=[]
    n = int(input("Podaj liczbę n"))
    for i in range(1,n+1):
        lista.append(i*i)
    print(lista)

def zadanie5():
    lista=[]
    n = int(input("Podaj liczbę n"))
    for i in range(1,n+1):
        if(n%i == 0 ):
            lista.append(i)
    print(lista)

zadanie5()