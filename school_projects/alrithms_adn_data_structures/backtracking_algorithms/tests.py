from algorithms import *
import time
import threading
import sys


sys.setrecursionlimit(2**31-31)
threading.stack_size(2**26)

def main():
    #zakres danych
    rng = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    rng2 = [10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    t = 0

    file = open('results.txt', 'a')

    '''###############     Czasy algorytmow w zaleznosci od ilosci elementow dla grafu nieskierowanego     ##################
    file.write('Czasy algorytmow w zaleznosci od ilosci elementow dla grafu nieskierowanego\n')
    file.write('alg/n,10,50,100,150,200,250,300,350,400,450,500\n')

    ###########     hamilton
    file.write('H')
    for n in rng:
        for i in range(5):
            g = generateRandomGraph(n, 0.5)
            m = createNeighbourMatrix(g)
            start = time.time()
            result = Hcycle(m, 'n')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t/5)*10000)))
        t = 0
    file.write('\n')

    ###########     euler
    file.write('E')
    for n in rng:
        for i in range(5):
            g = generateRandomGraph(n, 0.5)
            m = createNeighbourMatrix(g)
            start = time.time()
            result = searchForEuler(m)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 5) * 10000)))
        t = 0
    file.write('\n')

    ###############     Czasy algorytmow w zaleznosci od ilosci elementow dla grafu skierowanego     ##################
    file.write('Czasy algorytmow w zaleznosci od ilosci elementow dla grafu skierowanego\n')
    file.write('alg/n,10,50,100,150,200,250,300,350,400,450,500\n')
    ###########     hamilton
    file.write('H')
    for n in rng:
        for i in range(3):
            g = generateRandomDiGraph(n, 0.8)
            l = createNextList(g)
            start = time.time()
            result = Hcycle(l, 'd')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     euler
    print("---------------------------------------------------------------")
    file.write('E')
    for n in rng:
        for i in range(3):
            g = generateRandomDiGraph(n, 0.8)
            l = createNextList(g)
            start = time.time()
            result = searchForDiEuler(l)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###############     porownanie czasow hamiltona dla grafu skierowanego i nieskierowanego     ##################
    file.write('porownanie czasow hamiltona dla grafu skierowanego i nieskierowanego\n')
    file.write('alg/n,10,30,60,90,120,150,180,210,240,270,300\n')

    ###########     nieskierowany
    file.write('N')
    for n in rng2:
        for i in range(3):
            g = generateRandomGraph(n, 0.8)
            m = createNeighbourMatrix(g)
            start = time.time()
            result = Hcycle(m, 'n')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     skierowany
    print("---------------------------------------------------------------")
    file.write('D')
    for n in rng2:
        for i in range(3):
            g = generateRandomDiGraph(n, 0.8)
            m = createNextList(g)
            start = time.time()
            result = Hcycle(m, 'd')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###############     porownanie czasow eulera dla grafu skierowanego i nieskierowanego     ##################
    file.write('porownanie czasow eulera dla grafu skierowanego i nieskierowanego\n')
    file.write('alg/n,10,30,60,90,120,150,180,210,240,270,300\n')

    ###########     nieskierowany
    print("---------------------------------------------------------------")
    file.write('N')
    for n in rng2:
        for i in range(3):
            g = generateRandomGraph(n, 0.5)
            l = createNeighbourMatrix(g)
            start = time.time()
            result = searchForEuler(l)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     skierowany
    print("---------------------------------------------------------------")
    file.write('D')
    for n in rng2:
        for i in range(3):
            g = generateRandomDiGraph(n, 0.5)
            l = createNextList(g)
            start = time.time()
            result = searchForDiEuler(l)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###############     porownanie czasow alorytmow dla grafu nieskierowanego w zaleznosci od nasycenia     ##################
    file.write('porownanie czasow alorytmow dla grafu nieskierowanego w zaleznosci od nasycenia\n')
    file.write('alg/n,10,20,30,40,50,60,70,80,90\n')
    rng3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    ###########     hamilton
    file.write('H')
    for n in rng3:
        for i in range(3):
            g = generateRandomGraph(1000, n)
            m = createNeighbourMatrix(g)
            start = time.time()
            result = Hcycle(m, 'n')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     euler
    print("---------------------------------------------------------------")
    file.write('E')
    for n in rng3:
        for i in range(3):
            g = generateRandomGraph(1000, n)
            m = createNeighbourMatrix(g)
            start = time.time()
            result = searchForEuler(m)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###############     porownanie czasow alorytmow dla grafu skierowanego w zaleznosci od nasycenia     ##################
    file.write('porownanie czasow alorytmow dla grafu skierowanego w zaleznosci od nasycenia\n')
    file.write('alg/n,10,20,30,40,50,60,70,80,90\n')

    ###########     hamilton
    print("---------------------------------------------------------------")
    file.write('H')
    for n in rng3:
        for i in range(3):
            g = generateRandomDiGraph(250, n)
            l = createNextList(g)
            start = time.time()
            result = Hcycle(l, 'd')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     euler
    print("---------------------------------------------------------------")
    file.write('E')
    for n in rng3:
        for i in range(3):
            g = generateRandomDiGraph(250, n)
            l = createNextList(g)
            start = time.time()
            result = searchForDiEuler(l)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')'''

    ###############     porownanie czasow hamiltona dla grafu skierowanego i nieskierowanego     ##################
    file.write('porownanie czasow hamiltona dla grafu skierowanego i nieskierowanego w zaleznosci od nasyzcenia\n')
    file.write('alg/n,10,20,30,40,50,60,70,80,90\n')
    rng3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    ###########     nieskierowany
    file.write('N')
    for n in rng3:
        for i in range(3):
            g = generateRandomGraph(250, n)
            m = createNeighbourMatrix(g)
            start = time.time()
            result = Hcycle(m, 'n')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     skierowany
    print("---------------------------------------------------------------")
    file.write('D')
    for n in rng3:
        for i in range(3):
            g = generateRandomDiGraph(250, n)
            m = createNextList(g)
            start = time.time()
            result = Hcycle(m, 'd')
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    '''###############     porownanie czasow eulera dla grafu skierowanego i nieskierowanego     ##################
    file.write('porownanie czasow eulera dla grafu skierowanego i nieskierowanego\n')
    file.write('alg/n,10,30,60,90,120,150,180,210,240,270,300\n')

    ###########     nieskierowany
    print("---------------------------------------------------------------")
    file.write('N')
    for n in rng3:
        for i in range(3):
            g = generateRandomGraph(250, n)
            l = createNeighbourMatrix(g)
            start = time.time()
            result = searchForEuler(l)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ###########     skierowany
    print("---------------------------------------------------------------")
    file.write('D')
    for n in rng3:
        for i in range(3):
            g = generateRandomDiGraph(250, n)
            l = createNextList(g)
            start = time.time()
            result = searchForDiEuler(l)
            stop = time.time()
            t += stop - start
            print(i)
        file.write(',' + str(int((t / 3) * 10000)))
        t = 0
    file.write('\n')

    ################################        wykres 3D dla skierowanego hamiltona ###########################
    file.write("wykres 3D dla skierowanego hamiltona\n")
    file.write("s/n,10,30,60,90,120,150,180,210,240,270,300\n")
    rng4 = [10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    rng5 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for s in rng5:
        file.write(str(s))
        for n in rng4:
            for i in range(3):
                g = generateRandomDiGraph(n, s)
                l = createNextList(g)
                start = time.time()
                result = Hcycle(l, 'd')
                stop = time.time()
                t += stop - start
                print(i)
            file.write(',' + str(int((t / 3) * 10000)))
            t = 0
        file.write('\n')
    file.write('\n')

    ################################        wykres 3D dla nieskierowanego hamiltona ###########################
    file.write("wykres 3D dla skierowanego hamiltona\n")
    file.write("s/n,10,30,60,90,120,150,180,210,240,270,300\n")
    rng4 = [10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    rng5 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for s in rng5:
        file.write(str(s))
        for n in rng4:
            for i in range(3):
                g = generateRandomGraph(n, s)
                m = createNeighbourMatrix(g)
                start = time.time()
                result = Hcycle(m, 'n')
                stop = time.time()
                t += stop - start
                print(i)
            file.write(',' + str(int((t / 3) * 10000)))
            t = 0
        file.write('\n')
    file.write('\n')

    ################################        wykres 3D dla skierowanego eulera ###########################
    file.write("wykres 3D dla nieskierowanego eulerra\n")
    file.write("s/n,10,30,60,90,120,150,180,210,240,270,300\n")
    rng4 = [10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    rng5 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for s in rng5:
        file.write(str(s))
        for n in rng4:
            for i in range(3):
                g = generateRandomDiGraph(n, s)
                l = createNextList(g)
                start = time.time()
                result = searchForDiEuler(l)
                stop = time.time()
                t += stop - start
                print(i)
            file.write(',' + str(int((t / 3) * 10000)))
            t = 0
        file.write('\n')
    file.write('\n')

    ################################        wykres 3D dla nieskierowanego eulera ###########################
    file.write("wykres 3D dla nieskierowanego eulerra\n")
    file.write("s/n,10,30,60,90,120,150,180,210,240,270,300\n")
    rng4 = [10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    rng5 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for s in rng5:
        file.write(str(s))
        for n in rng4:
            for i in range(3):
                g = generateRandomGraph(n, s)
                m = createNeighbourMatrix(g)
                start = time.time()
                result = searchForEuler(m)
                stop = time.time()
                t += stop - start
                print(i)
            file.write(',' + str(int((t / 3) * 10000)))
            t = 0
        file.write('\n')
    file.write('\n')'''


    file.close()





thread = threading.Thread(target=main)
thread.start()