import threading
from sort import *
import sort as s
from functions import *
import time
import sys
# w pliku sort.py zdefiniowane sa zmienne por i zam
# odpowiadajace za zliczanie ilosc porownan i zamian

#caly program byl wykonywany czesciami i kolejne segmenty byly dopisywane do plikow z danymi

sys.setrecursionlimit(10**6)        #cały program musi byc uruchomiony jako wątek
threading.stack_size(2**26)         #ze wzgledu na koniecznosc powiekszenia stosu
def f():    #glowny program
    czas=0
    operacje=0
    file1 = open("alghoritm_times.txt", "a")    #zawiera zaleznosc czasu wykonywania od ilosci danych
    file2 = open("operation_quantity.txt", "a")         # zawiera zaleznosc ilosci operacji od ilosci danych
    """file1.write("zaleznosc czasu od ilosci danych\n")
    file2.write("zaleznosc ilosci operacji od ilosci danych\n")
    
    ##quicksort#################################################################################
    n=[500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    file1.write("TESTY QUICK SORT\n")
    file1.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    file2.write("TESTY QUICK SORT\n")
    file2.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    
    file1.write("random,")   #dane losowe#################
    file2.write("random,")
    for i in n:
        for j in range(10):
            l=generate_random(i)
            start=time.time()
            quick_sort(l,0,len(l)-1)
            stop=time.time()
            czas+=stop-start
    
        operacje=(s.zam+s.por)//10
        czas=czas/10
        file1.write(str(rnd(czas,5)) + "," )
        file2.write(str(operacje) + "," )
        s.zam=0
        s.por=0
        czas=0
    file1.write("\n")
    file2.write("\n")

    file1.write("rising,")   #dane rosnące#########################
    file2.write("rising,")
    for i in n:
        for j in range(10):
            l=generate_rise(i)
            start=time.time()
            quick_sort(l,0,len(l)-1)
            stop=time.time()
            czas+=stop-start

        operacje=(s.zam+s.por)//10
        czas=czas/10
        file1.write(str(rnd(czas,5)) + "," )
        file2.write(str(operacje) + "," )
        s.zam=0
        s.por=0
        czas=0
    file1.write("\n")
    file2.write("\n")

    file1.write("decreasing,")   #dane malejace#########################
    file2.write("decreasing,")
    for i in n:
        for j in range(10):
            l=generate_decrease(i)
            start=time.time()
            quick_sort(l,0,len(l)-1)
            stop=time.time()
            czas+=stop-start

        operacje=(s.zam+s.por)//10
        czas=czas/10
        file1.write(str(rnd(czas,5)) + "," )
        file2.write(str(operacje) + "," )
        s.zam=0
        s.por=0
        czas=0
    file1.write("\n")
    file2.write("\n")

    file1.write("A_shape,")   #dane A ksztaltne#########################
    file2.write("A_shape,")
    for i in n:
        for j in range(10):
            l=generate_Ashape(i)
            start=time.time()
            quick_sort(l,0,len(l)-1)
            stop=time.time()
            czas+=stop-start

        operacje=(s.zam+s.por)//10
        czas=czas/10
        file1.write(str(rnd(czas,5)) + "," )
        file2.write(str(operacje) + "," )
        s.zam=0
        s.por=0
        czas=0
    file1.write("\n")
    file2.write("\n")

    file1.write("V_shape,")   #dane V ksztaltne#########################
    file2.write("V_shape,")
    for i in n:
        for j in range(10):
            l=generate_Vshape(i)
            start=time.time()
            quick_sort(l,0,len(l)-1)
            stop=time.time()
            czas+=stop-start

        operacje=(s.zam+s.por)//10
        czas=czas/10
        file1.write(str(rnd(czas,5)) + "," )
        file2.write(str(operacje) + "," )
        s.zam=0
        s.por=0
        czas=0
    file1.write("\n")
    file2.write("\n")

    ##mergesort#################################################################################
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    file1.write("TESTY MERGE SORT\n")
    file1.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    file2.write("MERGE SORT\n")
    file2.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")

    file1.write("random,")  # dane losowe#################
    file2.write("random,")
    for i in n:
        for j in range(10):
            l = generate_random(i)
            start = time.time()
            merge_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")
    
    file1.write("rising,")  # dane rosnące#########################
    file2.write("rising,")
    for i in n:
        for j in range(10):
            l = generate_rise(i)
            start = time.time()
            merge_sort(l)
            stop = time.time()
            czas += stop - start
    
        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")
    
    file1.write("decreasing,")  # dane malejace#########################
    file2.write("decreasing,")
    for i in n:
        for j in range(10):
            l = generate_decrease(i)
            start = time.time()
            merge_sort(l)
            stop = time.time()
            czas += stop - start
    
        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")
    
    file1.write("A_shape,")  # dane A ksztaltne#########################
    file2.write("A_shape,")
    for i in n:
        for j in range(10):
            l = generate_Ashape(i)
            start = time.time()
            merge_sort(l)
            stop = time.time()
            czas += stop - start
    
        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")
    
    file1.write("V_shape,")  # dane V ksztaltne#########################
    file2.write("V_shape,")
    for i in n:
        for j in range(10):
            l = generate_Vshape(i)
            start = time.time()
            merge_sort(l)
            stop = time.time()
            czas += stop - start
    
        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    ##heapsort##################################################################################
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    file1.write("TESTY HEAP SORT\n")
    file1.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    file2.write("HEAP SORT\n")
    file2.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")

    file1.write("random,")  # dane losowe#################
    file2.write("random,")
    for i in n:
        for j in range(10):
            l = generate_random(i)
            start = time.time()
            heap_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("rising,")  # dane rosnące#########################
    file2.write("rising,")
    for i in n:
        for j in range(10):
            l = generate_rise(i)
            start = time.time()
            heap_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("decreasing,")  # dane malejace#########################
    file2.write("decreasing,")
    for i in n:
        for j in range(10):
            l = generate_decrease(i)
            start = time.time()
            heap_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("A_shape,")  # dane A ksztaltne#########################
    file2.write("A_shape,")
    for i in n:
        for j in range(10):
            l = generate_Ashape(i)
            start = time.time()
            heap_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("V_shape,")  # dane V ksztaltne#########################
    file2.write("V_shape,")
    for i in n:
        for j in range(10):
            l = generate_Vshape(i)
            start = time.time()
            heap_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    ##insertionsort##############################################################################
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    file1.write("TESTY INSERTION SORT\n")
    file1.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    file2.write("INSERTION SORT\n")
    file2.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")

    file1.write("random,")  # dane losowe#################
    file2.write("random,")
    for i in n:
        for j in range(10):
            l = generate_random(i)
            start = time.time()
            insertion_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("rising,")  # dane rosnące#########################
    file2.write("rising,")
    for i in n:
        for j in range(10):
            l = generate_rise(i)
            start = time.time()
            insertion_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("decreasing,")  # dane malejace#########################
    file2.write("decreasing,")
    for i in n:
        for j in range(10):
            l = generate_decrease(i)
            start = time.time()
            insertion_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("A_shape,")  # dane A ksztaltne#########################
    file2.write("A_shape,")
    for i in n:
        for j in range(10):
            l = generate_Ashape(i)
            start = time.time()
            insertion_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("V_shape,")  # dane V ksztaltne#########################
    file2.write("V_shape,")
    for i in n:
        for j in range(10):
            l = generate_Vshape(i)
            start = time.time()
            insertion_sort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    ##bubblesort##############################################################################
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    file1.write("TESTY BUBBLE SORT\n")
    file1.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    file2.write("BUBBLE SORT\n")
    file2.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")

    file1.write("random,")  # dane losowe#################
    file2.write("random,")
    for i in n:
        for j in range(10):
            l = generate_random(i)
            start = time.time()
            BubbleSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("rising,")  # dane rosnące#########################
    file2.write("rising,")
    for i in n:
        for j in range(10):
            l = generate_rise(i)
            start = time.time()
            BubbleSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("decreasing,")  # dane malejace#########################
    file2.write("decreasing,")
    for i in n:
        for j in range(10):
            l = generate_decrease(i)
            start = time.time()
            BubbleSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("A_shape,")  # dane A ksztaltne#########################
    file2.write("A_shape,")
    for i in n:
        for j in range(10):
            l = generate_Ashape(i)
            start = time.time()
            BubbleSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("V_shape,")  # dane V ksztaltne#########################
    file2.write("V_shape,")
    for i in n:
        for j in range(10):
            l = generate_Vshape(i)
            start = time.time()
            BubbleSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    ##selectionsort##############################################################################
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    file1.write("TESTY SELECTION SORT\n")
    file1.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")
    file2.write("SELECTION SORT\n")
    file2.write("dane,500,1000,1500,2000,2500,3000,3500,4000,4500,5000\n")

    file1.write("random,")  # dane losowe#################
    file2.write("random,")
    for i in n:
        for j in range(10):
            l = generate_random(i)
            start = time.time()
            SelectionSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("rising,")  # dane rosnące#########################
    file2.write("rising,")
    for i in n:
        for j in range(10):
            l = generate_rise(i)
            start = time.time()
            SelectionSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("decreasing,")  # dane malejace#########################
    file2.write("decreasing,")
    for i in n:
        for j in range(10):
            l = generate_decrease(i)
            start = time.time()
            SelectionSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("A_shape,")  # dane A ksztaltne#########################
    file2.write("A_shape,")
    for i in n:
        for j in range(10):
            l = generate_Ashape(i)
            start = time.time()
            SelectionSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.write("V_shape,")  # dane V ksztaltne#########################
    file2.write("V_shape,")
    for i in n:
        for j in range(10):
            l = generate_Vshape(i)
            start = time.time()
            SelectionSort(l)
            stop = time.time()
            czas += stop - start

        operacje = (s.zam + s.por) // 10
        czas = czas / 10
        file1.write(str(rnd(czas, 5)) + ",")
        file2.write(str(operacje) + ",")
        s.zam = 0
        s.por = 0
        czas = 0
    file1.write("\n")
    file2.write("\n")

    file1.close()
    file2.close()"""

    #####ulozenie danych do stworzenia wykresow dla rodzajow danych wejsciowych####
    file1 = open("alghoritm_times.txt","r")
    file2 = open("data_times.txt","w")
    file2.write("dane dla rodzajow danych\n")
    a=["quickSort","mergeSort","heapSort","insertionSort","bubbleSort","selectionSort"]
    lines=[]
    for line in file1.readlines():
        lines.append(line)
    i=0
    ##dane losowe
    file2.write("DANE LOSOWE\n")
    for line in lines:
        line_list = line.split(sep=",")
        if line_list[0]=="random":
            file2.write(a[i] + "," + ",".join(line_list[1:]))
            i += 1
    i = 0
    ##dane rosnace
    file2.write("DANE ROSNACE\n")
    for line in lines:
        line_list = line.split(sep=",")
        if line_list[0] == "rising":
            file2.write(a[i] + "," + ",".join(line_list[1:]))
            i += 1
    i = 0
    ##dane malejace
    file2.write("DANE MALEJACE\n")
    for line in lines:
        line_list = line.split(sep=",")
        if line_list[0] == "decreasing":
            file2.write(a[i] + "," + ",".join(line_list[1:]))
            i += 1
    i = 0
    #dane A ksztaltne
    file2.write("DANE A KSZTALTNE\n")
    for line in lines:
        line_list = line.split(sep=",")
        if line_list[0] == "A_shape":
            file2.write(a[i] + "," + ",".join(line_list[1:]))
            i += 1
    i = 0
    ##dane V ksztaltne
    file2.write("DANE V KSZTALTNE\n")
    for line in lines:
        line_list = line.split(sep=",")
        if line_list[0] == "V_shape":
            file2.write(a[i] + "," + ",".join(line_list[1:]))
            i += 1

    file1.close()
    file2.close()
##koniec programu

x=threading.Thread(target=f)
x.start()