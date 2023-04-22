import networkx as nx
import time
from graphs import *
#zakres danych
d = [150, 300, 450, 600, 750, 900, 1050, 1200, 1350, 1500]
file = open('result.txt', 'a')
#file.write('alg/n,150,300,450,600,750,900,1050,1200,1350,1500\n')

#przyblizenie liczby do n miejsc po przecinku
def rnd(x,n):
    multipler=10**n
    x=x*multipler
    x=round(x)
    return x/multipler

#funkcja zapisujaca dane grafu do pliku
#n-wierzcholkow, g - graf, fname- nazwa pliku
def export_grapf_to_file(n, graph, fname):
    data = open(fname, 'w')
    data.write(str(n) + ' ' + str(n-1))
    for i in graph.edges:
        data.write(str(i[0] + 1) + ' ')
        data.write(str(i[1] + 1) + '\n')
    data.close()

'''##DFS macierz somsiedztwa:
file.write('DEF_m/n')
for elem in d:
    t = 0
    for i in range(3):
        g = nx.gnr_graph(elem, 0.5)
        export_grapf_to_file(elem, g, 'data.txt')
        start = time.time()
        m = create_neighbour_matrix('data.txt')
        s = DFS_neighbour_matrix(m)
        stop = time.time()
        t += stop - start
    file.write(',' + str(rnd(t/3, 5)))
file.write('\n')

##DEL macierz somsiedztwa:
file.write('DEL_m/n')
for elem in d:
    t = 0
    for i in range(3):
        g = nx.gnr_graph(elem, 0.5)
        export_grapf_to_file(elem, g, 'data.txt')
        start = time.time()
        m = create_neighbour_matrix('data.txt')
        s = DEL_neighbour_matrix(m)
        stop = time.time()
        t += stop - start
    file.write(',' + str(rnd(t/3, 5)))
file.write('\n')

##DFS lista nastepnikow:
file.write('DFS_l/n')
for elem in d:
    t = 0
    for i in range(3):
        g = nx.gnr_graph(elem, 0.5)
        export_grapf_to_file(elem, g, 'data.txt')
        start = time.time()
        l = next_list('data.txt')
        s = DFS_for_next_list(l)
        stop = time.time()
        t += stop - start
    file.write(',' + str(rnd(t/3, 5)))
file.write('\n')'''

##DEL lista nastepnikow:
file.write('DEL_l/n')
for elem in d:
    t = 0
    for i in range(3):
        g = nx.gnr_graph(elem, 0.5)
        export_grapf_to_file(elem, g, 'data.txt')
        l = next_list('data.txt')
        start = time.time()
        s = DEL_for_next_list(l)
        stop = time.time()
        t += stop - start
    file.write(',' + str(rnd(t/3, 5)))
file.write('\n')

file.close()
