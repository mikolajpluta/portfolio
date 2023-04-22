from functions import *
##algorytmy rozwiazujace problem plecakowy
##dane podane sa w mpostaci listy krotek z czego pierwsza z nich jest postaci (n, c), gdzie n - ilosc elementow w zbiorze,
## c - pojemnosc plecaka. kolejne krotki to elementy postaci (w, p), gdzie w - waga, p - wartosc.
## id kazdego elementu odpowiada indekswoi na liscie (1...n)

###########################     algorytm siłowy     #############################

#funkcja liczaca sume wag elementow w plecaku, elems - lista z danymi bez pierwszego elementu, czyli same obiekty w zbiorze
#x - odwrócona liczba zapisana binarnie reprezentujaca elementy ktore są w plecaku
def sumWeight(x, elems):
    sum = 0
    for i in range(len(x)):
       sum += int(x[i]) * elems[i][0]
    return sum
#funkcja liczaca sume wartosci elementow w plecaku, dziala analogicznie do sumWeight
def sumPrice(x, elems):
    sum = 0
    for i in range(len(x)):
       sum += int(x[i]) * elems[i][1]
    return sum

#data - lista z danymi
def knapscakBruteForce(data):
    n = data[0][0]  #liczba elementow w zbiorze
    c = data[0][1]  #pojemnosc plecaka
    result = ''     #wynik, ciag 0 i 1, 1 na i-tej pozycji oznacza, ze i-ty element jest w plecaku(numercja od 1)
    fMax = 0    #maksymalna znaleziona suma wartosci
    for i in range(1, 2**n):
        x = "{0:b}".format(i)[-1::-1]   #liczba i w postaci binarnej i odwrócona
        Wx = sumWeight(x, data[1:])     #suma wag elementow w plecaku
        if Wx <= c:
            Fx = sumPrice(x, data[1:])  #suma wartosci elementow w plecaku
            if Fx >= fMax:
                fMax = Fx
                result = x
    #wypisanie wyniku
    #print("calkowity rozmiar:", sumWeight(result, data[1:]))
    #print("calkowita wartosc:", sumPrice(result, data[1:]))
    return result

###########################     algorytm zachlanny     #############################
#funkcje sumowana na potrzeby wyswietlenia
def sumWeight2(elems, data):
    sum = 0
    for elem in elems:
        sum += data[elem][0]
    return sum

def sumPrice2(elems, data):
    sum = 0
    for elem in elems:
        sum += data[elem][1]
    return sum

#####   id obiektu to jego index w poczatkowej liscie (1...n)
def knapsackGreedy(data):
    dataCopy = data.copy()     #potrzebne do wypisania wynikiu, poniewaz lista jest edytowana w trakcie wykonywania
    n = data[0][0]
    c = data[0][1]
    result = []     #zawartosc plecaka
    freeSpace = c   #wolne miejsce w plecaku
    items = sorted(data[1:], key=lambda x: x[1]/x[0], reverse=True)     #obiekty posortowane nierosnąco wzgledem wartosc/masa
    for item in items:
        if item[0] <= freeSpace:    #jezeli jest miejsce w plecaku
            result.append(dataCopy[1:].index(item)+1)     #dodaj obiekt do wyniku   #data[1:] zeby nie uwzglednialo danych c i n
            dataCopy[result[-1]] = (0, 0)            #zastapinie obiektu zerami aby funkcja .index nie powielkala tego samego wyniku
            freeSpace -= item[0]
    #wypisanie wyniku
    #print("calkowity rozmiar:", sumWeight2(result, data))
    #print("calkowita wartosc:", sumPrice2(result, data))
    return result

###########################     algorytm dynamiczny     #############################
def knapsackDynamic(data):
    n = data[0][0]
    c = data[0][1]
    result = []
    matrix = []     #przyugotoanie macierzy (n+1)X(c+1)
    for i in range(n+1):    #pierwszy wiersz i pierwsza kolumna to 0, reszta None
        matrix.append([])
        for j in range(c+1):
            matrix[i].append(0)

    ###wypelnianie macierzy kosztow
    for i in range(1, n+1):     #dla kazdej komórki macierzy poza 0 kolumna i 0 wierszem
        for j in range(1, c+1):
            if data[i][0] > j:  #jesli waga i-tego elementu jest wieksza od pojemnosci j
                matrix[i][j] = matrix[i-1][j]
            else:               #kiedy element miesci sie do plecaka
                matrix[i][j] = max(matrix[i-1][j], matrix[i - 1][j - data[i][0]] + data[i][1])

    ##odczyt rozwiazania
    while(n > 0):
        if matrix[n][c] > matrix[n-1][c]:       #jako zmienne pomocnicze wykorzystujemy n i c, poniewaz juz dluzej nie sa potrzebne
            result.append(n)
            c -= data[n][0]
        n -= 1

    # wypisanie wyniku
    #print("calkowity rozmiar:", sumWeight2(result, data))
    #print("calkowita wartosc:", sumPrice2(result, data))
    return result


