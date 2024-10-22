import networkx as nx
import matplotlib.pyplot as plt
import time

##dwie metody reprezentacji grafu:
#1 macierz sasiedztwa
#2 lista nastepnikow

#### funkcja zwracajaca macierz sasiedztwa utworzoną z pliku podanego jako parametr
def create_neighbour_matrix(name):  #jako parametr podajemy nazwe pliku
    file = open(name, 'r')
    size =[int(x) for x in file.readline().split()]
    matrix = []
    for i in range(size[0]):
        matrix.append([])
        for j in range(size[0]):
            matrix[i].append(0)


    for line in file.readlines():
        v = [int(x) for x in line.split()]
        matrix[v[0]-1][v[1]-1] = 1
        matrix[v[1]-1][v[0]-1] = -1
    file.close()
    return matrix

#tworzenie listy następników dla grafu
def next_list(name):
    file = open(name, 'r')
    data = []
    for line in file.readlines():
        data.append([int(x) for x in line.split()])
    file.close()

    next_list = []
    for i in range(1, data[0][0] + 1):
        vnext = [i]  # tymczasowa lista nastepnikow danego wierzcholka
        for pair in data[1:]:
            if pair[0] == i:
                vnext.append(pair[1])
        vnext[1:] = sorted(vnext[1:])
        next_list.append(vnext)
    return next_list

## tworzenie listy poprzednikow dla grafu
def previous_list(name):
    file = open(name, 'r')
    data = []
    for line in file.readlines():
        data.append([int(x) for x in line.split()])
    file.close()
    previous_list = []
    for i in range(1, data[0][0] + 1):
        vprevious = [i]  # tymczasowa lista poprzednikow danego wierzcholka
        for pair in data[1:]:
            if pair[1] == i:
                vprevious.append(pair[0])
        vprevious[1:] = sorted(vprevious[1:])
        previous_list.append(vprevious)
    return previous_list


#twoorzenie macierzy grafu
'''def create_graph_matrix(name):
    file = open(name, 'r')
    data = []
    for line in file.readlines():
        data.append([int(x) for x in line.split()])
    file.close()

    #lista nastepnikow
    next_list = []
    for i in range(1, data[0][0]+1):
        vnext = [i]     #tymczasowa lista nastepnikow danego wierzcholka
        for pair in data[1:]:
            if pair[0] == i:
                vnext.append(pair[1])
        vnext[1:] = sorted(vnext[1:])
        next_list.append(vnext)

    #lista poprzednikow
    previous_list = []
    for i in range(1, data[0][0]+1):
        vprevious = [i]     #tymczasowa lista poprzednikow danego wierzcholka
        for pair in data[1:]:
            if pair[1] == i:
                vprevious.append(pair[0])
        vprevious[1:] = sorted(vprevious[1:])
        previous_list.append(vprevious)

    #lista braku incydencji
    noIncident_list = []
    for i in range(1, data[0][0]+1):
        vnoIncident = [i]       #tymczasowalista wierzcholkow nieincydentnych dla danego wierzcholka
        for j in range(1, data[0][0]+1):
            if not j in next_list[i-1][1:] and not j in previous_list[i-1][1:]:
                vnoIncident.append(j)
        vnoIncident[1:] = sorted(vnoIncident[1:])
        noIncident_list.append(vnoIncident)

    #macierz
    matrix = []
    #wyelnienie macierzy zearami
    for i in range(data[0][0]):
        matrix.append([])
        for j in range(data[0][0] + 3):
            matrix[i].append(0)
    #dalsze wypelnianie maciezrzy
    for i in range(data[0][0]):
        #obsluga listy nastepnikow
        for j in next_list[i][1:]:
            matrix[i][j-1] = next_list[i][-1]
        matrix[i][data[0][0]] = next_list[i][1]
        #obsulga listy poprzednikow
        for j in previous_list[i][1:]:
            matrix[i][j-1] = previous_list[i][-1] + data[0][0]
        matrix[i][data[0][0]+1] = previous_list[i][1]
        #obsluga isty nieincydentnych
        for j in noIncident_list[i][1:]:
            matrix[i][j-1] = -(noIncident_list[i][-1])
        matrix[i][data[0][0]+2] = noIncident_list[i][1]
    return matrix'''
#algorytm DFS dla macierzy somsiedztwa`
def DFS_neighbour_matrix(matrix):
    current = 1
    #wybor pierwszego wierzcholka
    for i in range(len(matrix)):
        if not -1 in matrix[i]:
            current = i+1
            break
    queue = []
    stack = []
    res = []
    while len(matrix) > len(stack):
        for i in range(len(matrix)):
            if matrix[current-1][i] == 1 and i+1 not in stack:
                if i+1 in queue:
                    print("graf zawiera petle, sortowanie niemozliwe")
                    return
                queue.append(current)
                current = i+1
                break
        help = 1
        for i in range(len(matrix)):
            if matrix[current-1][i] == 1 and i+1 not in stack:
                help = 0
                break
        if help == 1:
            stack.append(current)
            if len(queue) > 0:
                current = queue.pop()
            else:
                for i in range(len(matrix)):        #ponowny wybor pierwszego wierzcholka, jesli jest wiecejniz 1
                    if not -1 in matrix[i] and not i+1 in stack:    #z zerowym stopniem wejsciowym
                        current = i + 1
                        break

    return stack[-1::-1]

#algorytm DEL dla macierzy somsiedztwa
def DEL_neighbour_matrix(matrix):
    res = []
    current = 1
    while len(res) < len(matrix):
        for i in range(len(matrix)):
            help = 0
            if not -1 in matrix[i] and not i+1 in res:
                current = i+1
                res.append(current)
                help += 1
                break
        if help == 0:
            print('cykl')
            return

        for i in range(len(matrix)):
            matrix[i][current-1] = 0
    return res

#fuunkcja pomocnicza zwracajaca pierwszy wierzcholek z zerowym stopniem wejsciowym,
# którego nie ma w lisci epodanej jako parametr(dla listy nasteonikow
def first_node(next_list, data_list):
    for i in range(1,len(next_list)+1):
        tmp = 1
        if i in data_list:
            continue
        for j in range(1,len(next_list)):
            if i in next_list[j][1:]:
                tmp = 0
                break
        if tmp == 1:
            return i
    return 0

# algorytm DFS dla listy nastepnikow
def DFS_for_next_list(list):
    stack = []
    queue = []
    current = first_node(list,[])
    while len(list) > len(stack):
        while len(list[current-1]) > 1:
            if list[current-1][1] in stack:
                del list[current-1][1]
                continue
            queue.append(current)
            tmp = list[current-1][1]
            del list[current-1][1]
            current = tmp

        stack.append(current)
        if len(queue) > 0:
            current = queue.pop()
        else:
            current = first_node(list,stack)
        if current == 0:
            return stack[-1::-1]

#algorytm DEL dla listy nastepnikow
def DEL_for_next_list(list):
    stack = []
    while len(stack) < len(list):
        current = first_node(list, stack)
        stack.append(current)
        list[current-1] = [current]
    return stack

g = nx.gnr_graph(50, 0.5)
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos)
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_labels(g, pos)
plt.show()