import networkx as nx
import random
import matplotlib.pyplot as plt

#funkcja tworzaca losowy graf nieskierowany z n wierzcholkami,
#zwraca liste krotek, kazda krotka oznacza jedna krawedz
def generateRandomGraph(n ,p):
    g = nx.gnp_random_graph(n, p)
    while not nx.is_connected(g):
        g = nx.gnp_random_graph(n, p)
    data = [(n, len(g.edges))]
    return data + list(g.edges)

#generuje losowy graf skierowanym, zwraca lise lukow w postaci krotek
def generateRandomDiGraph(n, p):
    listOfTuples = generateRandomGraph(n, p)
    resultList = [listOfTuples[0]]     #funkcja przepisuje liste z grafu nieskierowanego i losowe krawedzie zamienia kolejnoscia w celu optymalizacji i lepszego rozkladu wylosowanego grafu
    for i in listOfTuples[1:]:
        r = random.randint(0, 1)
        if r == 0:
            resultList.append((i[0],i[1]))
        else:
            resultList.append((i[1], i[0]))
    return resultList

#generuje liste krotek z pliku
def generateGraphFromFile(fileName):
    result = []
    file = open(fileName, 'r')
    firstLine = file.readline()
    result.append((int(firstLine[0]), int(firstLine[2])))
    for line in file.readlines():
        result.append((int(line[0]), int(line[2])))
    file.close()
    return result

#funkcja tworzaca macierz grafu nieskierowanego, arkument - lista krotek z krawedziami
def createNeighbourMatrix(list):
    matrix = []
    size = list[0]
    for i in range(size[0]):
        matrix.append([])
        for j in range(size[0]):
            matrix[i].append(0)
    for edge in list[1:]:
        matrix[edge[0]][edge[1]] = 1
        matrix[edge[1]][edge[0]] = 1
    return matrix

#funkcja tworzaca liste nastepnikow grafu skierowanego, argument - lista krotek z lukami
def createNextList(list):
    result = []
    size = list[0]
    for i in range(size[0]):
        tmp = []
        for edge in list[1:]:
            if edge[0] == i:
                tmp.append(edge[1])
        tmp = sorted(tmp)
        result.append(tmp)
    return result

#funkcja wyswietlajaca graf nieskierowany, argument - lista krotek z krawedziami
def displayGraph(list):
    g = nx.empty_graph()
    g.add_edges_from(list[1:])
    pos = nx.spring_layout(g)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos)
    plt.show()

#funkcja wyswietlajaca graf skierowany, argument - lista krotek z krawedziami
def displayDiGraph(list):
    g = nx.DiGraph()
    g.add_edges_from(list[1:])
    pos = nx.spring_layout(g)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos)
    plt.show()
