from algorithms import *
import time

file = open('results.txt', 'a')
t = 0

'''########################        czas algorytmu silowego w zaleznosci od iloscvi elementow dla c=10       ##################
file.write("czas wykonywania algorytmu silowego\n")
file.write("n,10,11,12,13,14,15,16,17,18,19,20\n")
rng1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

file.write("silowy")
for n in rng1:
    for i in range(5):
        data = generateData(n, 10)
        start = time.time()
        res = knapscakBruteForce(data)
        stop = time.time()
        t += stop - start
    file.write("," + str(rnd(t/5, 3)))
    t = 0
file.write("\n")

########################        czas algorytmu zachlannego w zaleznosci od iloscvi elementow dla c=10       ##################
file.write("czas wykonywania algorytmu zachlannego\n")
file.write("n,2000,200000,400000,600000,800000,1000000,1200000,1400000,1600000,1800000\n")
rng2 = [2000, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000]

file.write("zachlanny")
for n in rng2:
    for i in range(5):
        data = generateData(n, 10)
        start = time.time()
        res = knapsackGreedy(data)
        stop = time.time()
        t += stop - start
    file.write("," + str(rnd(t/5, 3)))
    t = 0
file.write("\n")

########################        czas algorytmu dynamicznego w zaleznosci od iloscvi elementow dla c=10       ##################
file.write("czas wykonywania algorytmu dynamicznego\n")
file.write("n,2000,200000,400000,600000,800000,1000000,1200000,1400000,1600000,1800000\n")
rng3 = [2000, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000]

file.write("dynamiczny")
for n in rng3:
    for i in range(5):
        data = generateData(n, 10)
        start = time.time()
        res = knapsackDynamic(data)
        stop = time.time()
        t += stop - start
    file.write("," + str(rnd(t/5, 3)))
    t = 0
file.write("\n")

########################        czas algorytmu silowego w zaleznosci od pojemnosci plecaka dla n=18      ##################
file.write("czas wykonywania algorytmu silowego dla stalej pojemnosci\n")
file.write("c,10,1000,2000,3000,4000,5000,6000,7000,8000,9000\n")
rng4 = [10, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

file.write("silowy")
for c in rng4:
    for i in range(5):
        data = generateData(18, c)
        start = time.time()
        res = knapscakBruteForce(data)
        stop = time.time()
        t += stop - start
    file.write("," + str(rnd(t/5, 3)))
    t = 0
file.write("\n")

########################        czas algorytmu zachlannego w zaleznosci od pojemnosci plecaka dla n=200000     ##################
file.write("czas wykonywania algorytmu zachlannego\n")
file.write("c,10,1000,2000,3000,4000,5000,6000,7000,8000,9000\n")
rng5 = [10, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

file.write("zachlanny")
for c in rng5:
    for i in range(5):
        data = generateData(200000, c)
        start = time.time()
        res = knapsackGreedy(data)
        stop = time.time()
        t += stop - start
    file.write("," + str(rnd(t/5, 3)))
    t = 0
file.write("\n")

########################        czas algorytmu dynamicznego w zaleznosci od pojemnosci plecaka dla n=1000     ##################
file.write("czas wykonywania algorytmu dynamicznego\n")
file.write("c,10,1000,2000,3000,4000,5000,6000,7000,8000,9000\n")
rng6 = [10, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

file.write("dynamiczny")
for c in rng6:
    for i in range(5):
        data = generateData(1000, c)
        start = time.time()
        res = knapsackDynamic(data)
        stop = time.time()
        t += stop - start
    file.write("," + str(rnd(t/5, 3)))
    t = 0
file.write("\n")

####################        wykres 3D dla silowego      ###########################
file.write("czas wykonywania algorytmu silowego 3D\n")
file.write("c/n,2,8,12,16,20\n")
rng6 = [2, 8, 12, 16, 20]
rng7 = [10, 1000, 2000, 3000, 4000]

for c in rng7:
    file.write(str(c))
    for n in rng6:
        for i in range(3):
            data = generateData(n, c)
            start = time.time()
            res = knapscakBruteForce(data)
            stop = time.time()
            t += stop - start
        file.write("," + str(rnd(t / 3, 3)))
        t = 0
    file.write("\n")
file.write("\n")

####################        wykres 3D dla zachlannego      ###########################
file.write("czas wykonywania algorytmu zachlannego 3D\n")
file.write("c/n,1000,50000,100000,150000,200000\n")
rng8 = [1000, 50000, 100000, 150000, 200000]
rng9 = [10, 1000, 2000, 3000, 4000]

for c in rng9:
    file.write(str(c))
    for n in rng8:
        for i in range(3):
            data = generateData(n, c)
            start = time.time()
            res = knapsackGreedy(data)
            stop = time.time()
            t += stop - start
        file.write("," + str(rnd(t / 3, 3)))
        t = 0
    file.write("\n")
file.write("\n")'''

####################        wykres 3D dla dynamicznego      ###########################
file.write("czas wykonywania algorytmu dynamicznego 3D\n")
file.write("c/n,10,250,500,750,1000\n")
rng10 = [10, 250, 500, 750, 1000]
rng11 = [10, 1000, 2000, 3000, 4000]

for c in rng11:
    file.write(str(c))
    for n in rng10:
        for i in range(3):
            data = generateData(n, c)
            start = time.time()
            res = knapsackDynamic(data)
            stop = time.time()
            t += stop - start
        file.write("," + str(rnd(t / 3, 3)))
        t = 0
    file.write("\n")
file.write("\n")



'''file.close()
data = generateData(2000000, 10)
start = time.time()
res = knapsackDynamic(data)
stop = time.time()
print(stop - start)'''