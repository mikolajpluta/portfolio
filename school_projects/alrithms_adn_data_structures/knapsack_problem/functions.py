import random

####wczytywanie z pliku
def readDataFromFile(fileName):
    result = []
    file = open(fileName, 'r')
    for line in file.readlines():
        result.append(tuple(int(x) for x in line.split()))
    file.close()
    return result

#genererowanie listy danych dla n elementów i pojemności plecaka c
#wagi elementow losowane sa pomiedzy 1 - (0.7*c) a wartosci zawsze od 1 - 10
def generateData(n, c):
     result = [(n, c)]
     for i in range(n):
         result.append((random.randint(1, (0.7*c+1)//1), random.randint(1, 10)))
     return result

def rnd(x,n):
    multipler=10**n
    x=x*multipler
    x=round(x)
    return x/multipler

