import matplotlib.pyplot as plt
import networkx as nx
from functions import *
import time

#zmienne globalne na ktorych operuja funkcje
global O
global visited
global path
global start

#funkcja hamiltonian - pierwsza czesc algorytmu Robertsa-Floresa
#argumenty: v - wierzcholek, s - struktura grafu, t - tryb uruchomienia w zaleznosci od radzaju grafu
#'d' - skierowany 'n' - nieskierowany, dla danego typu grafu obsluguje inna strukture danych
def hamiltonian(v, s, t):
    global O
    global visited
    global path
    global start

    O[v] = True
    visited += 1

    #dla grafu nieskierowanego
    if t == 'n':
        for i in range(len(s)):
            if s[v][i] == 1:
                if i == start and visited == len(s):
                    return True
                if O[i] == False:
                    if hamiltonian(i, s, t):
                        path.append(i)
                        return True
    #dla grafu skerowanego
    if t =='d':
        for i in s[v]:
            if i == start and visited == len(s):
                return True
            if O[i] == False:
                if hamiltonian(i, s, t):
                    path.append(i)
                    return True

    O[v] = False
    visited -= 1
    return False

#druga czec algorytmu Robertsa-Floresa, zwraca liste wierzcholkow jesli istnieje cykl Hamiltona,
#wpp wypisuje komunikat o braku cyklu i zwraca false
#s - struktura danych, t - tryb
def Hcycle(s, t):
    global O
    global visited
    global path
    global start

    O = []
    for i in range(len(s)):
        O.append(False)
    path = [0]
    visited = 0
    start = 0
    isCycle = hamiltonian(start, s, t)
    if isCycle:
        return path[-1::-1]
    else:
        print("brak cyklu hamiltona")
        return False

#funkcja okreslajaca czy graf posiada cykl Eulera dla grafu nieskierowanego
#jako argument przyjmuje macierz sasiedztwa
def isEuler(m):
    #zanjdownaie 1 wierzcholka o stopniu niezerowym
    i = -1
    for j in range(len(m)):
        if 1 in m[j]:
            i = j
            break
    if i == -1:
        return True

    #inicjacja zmiennych pomocniczych
    no = 0
    S = []
    visited = []
    for j in range(len(m)):
        visited.append(False)

    #poczatek algorytmu
    S.append(i)
    visited[i] = True

    #uruchomienie DFS aby sprawdzic spojnosc i wyznaczyc stopnie wierzcholkow
    while len(S) > 0:
        v = S.pop()
        nc = 0
        for u in range(len(m)):
            if m[v][u] == 1:
                nc += 1
                if visited[u] == True:
                    continue
                visited[u] = True
                S.append(u)
        if nc % 2 == 1:
            no += 1

    #poszukiwanie jeszcze nieodwiedzonych wierzcholkow
    for j in range(i+1, len(m)-1):
        if visited[j] == False and 1 in m[j]:
            return False

    #jesli liczba nieparzystych wierzcholkow = 0, zwroc True, wpp False
    if no == 0:
        return True
    else:
        return False


#zmienna globalna do wyszukiwania cyklu Eulera
global stack
global m
global l
stack = []

#rekurencyjna funkcja wyszukujaca cykl eulera dla danego wierzcholka w grafie nieskierownaym
#m - macierz sasiedztwa grafu, v - obecny wierzcholek, poczatkowo bedzie to 0
def DFS_euler(v):
    global stack
    global m
    for i in range(len(m)):
        if m[v][i] == 1:
            m[v][i] = 0
            m[i][v] = 0
            DFS_euler(i)
    stack.append(v)

def searchForEuler(matrix):
    if not isEuler(matrix):
        print('brak cyklu Eulera')
        return False
    global m
    global stack
    m = matrix
    DFS_euler(0)
    result = []
    result = stack
    m = []
    stack = []
    return result

#poszukiwanie cyklu eulera dla grafu skierowanego
#zmienne globalne
global cvn
global VN
global Vlow
global VS
global Vin
global Vout
global C
global S
global l

#funkcja sprawzajaca czy w grafie znajduje sie cykl eulera
#argumentem jest lista nastepnikow
def DFSscc(v):
    global cvn
    global VN
    global Vlow
    global VS
    global Vin
    global Vout
    global C
    global S
    global l
    cvn += 1
    VN[v] = cvn
    Vlow[v] = cvn
    S.append(v)
    VS[v] = True
    for u in l[v]:
        Vout[v] = Vout[v] + 1
        Vin[u] = Vin[u] + 1
        if VN[u] != 0:
            if VS[u] == False:
                continue
            Vlow[v] = min(Vlow[v], VN[u])
            continue
        else:
            DFSscc(u)
            Vlow[v] = min(Vlow[v], Vlow[u])

    if Vlow[v] != VN[v]:
        return
    tmp = True
    while tmp:
        u = S.pop()
        VS[u] = False
        C[u] = v
        if u == v:
            tmp = False

def isDiEuler(list):
    global cvn
    global VN
    global Vlow
    global VS
    global Vin
    global Vout
    global C
    global S
    global l
    cvn = 0
    VN = []
    Vlow = []
    VS = []
    Vin = []
    Vout = []
    C = []
    S = []
    l = list
    tmp2 = True
    #przygotowanie zerowych tablic
    for i in range(len(l)):
        VN.append(0)
        Vlow.append(0)
        VS.append(False)
        Vin.append(0)
        Vout.append(0)
        C.append(0)

    for v in range(len(l)):
        if VN[v] == 0:
            DFSscc(v)

    v = 0
    while v < len(l) and Vin[v] + Vout[v] == 0:
        v += 1

    if v == len(l):
        return False

    cvn = C[v]
    cinout = 0
    coutin = 0
    while v < len(l):
        if Vin[v] + Vout[v] != 0:
            if C[v] != cvn:
                return False
            if Vin[v] != Vout[v]:
                if Vin[v] - Vout[v] == 1:
                    cinout += 1
                else:
                    coutin += 1
                    if coutin > 1:
                        return False
                    tmp1 = False
                if cinout > 1 and tmp2:
                    return False
                if Vout[v] - Vin[v] != 1 and tmp2:
                    return False
        v += 1

    if cinout == 1:
        return False
    return True

##funcja rekurencyjnie przechodzaca wszystkie krawedzie i odkladajaca wolne wierzcholki na stos
#opperuje na globalnej liscie nastepnikow
def DFS_DiEuler(v):
    global stack
    global m
    while len(m[v]) > 0:
        tmp = m[v][0]
        m[v] = m[v][1:]
        DFS_DiEuler(tmp)
    stack.append(v)

#funkcja ustwaijaca parametry globalne i uruchamijaca poszukiwanie sciezki eulera
def searchForDiEuler(list):
    if not isDiEuler(list):
        return False

    global m
    global stack
    m = list

    #wybr pierwszego wierzcholka z niezerowa liczba sasiadow
    v = 0
    for i in range(len(m)):
        if len(m[i]) > 0:
            v = i
            break

    DFS_DiEuler(v)
    result = []
    result = stack
    m = []
    stack = []
    return result[-1::-1]

