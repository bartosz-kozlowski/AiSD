import random
import time
import sys
import copy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
sys.setrecursionlimit(999999999)


def generator(n, saturation):
    v = [[0] * n for _ in range(n)]
    edges = 0
    totalEdges = int((n * (n - 1) / 2) * saturation)

    pom = list(range(n))
    random.shuffle(pom)

    for i in range(n - 1):
        v[pom[i + 1]][pom[i]] = 1
        v[pom[i]][pom[i + 1]] = 1
        edges += v[pom[i + 1]][pom[i]]

    v[pom[n - 1]][pom[0]] = 1
    v[pom[0]][pom[n - 1]] = 1
    edges += v[pom[n - 1]][pom[0]]

    while edges < totalEdges:
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        c = random.randint(0, n - 1)

        if a != b and a != c and b != c and not v[a][b] and not v[b][c] and not v[a][c]:
            v[a][b] = 1
            v[b][a] = 1
            v[b][c] = 1
            v[c][b] = 1
            v[a][c] = 1
            v[c][a] = 1
            edges += v[a][b] + v[b][c] + v[a][c]

    return v
def hamilton(graph, v, visited, path):
    visited[v] = True
    path.append(v)

    # Jeśli wszystkie wierzchołki zostały odwiedzone
    if len(path) == len(graph) and graph[v][0] == 1:
        # Cykl Hamiltona znaleziony
        #print("Cykl Hamiltona znaleziony:", path)
        return True

    # Sprawdzaj sąsiadów wierzchołka v
    for w in range(len(graph[v])):
        if graph[v][w] == 1 and not visited[w]:
            if hamilton(graph, w, visited, path):
                return True

    # Usuń wierzchołek v z ścieżki i oznacz jako nieodwiedzony
    path.pop()
    visited[v] = False

    return False


def find_hamiltonian_cycle(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    path = []

    # Przeszukiwanie grafu zaczynając od każdego wierzchołka
    for v in range(num_vertices):
        if hamilton(graph, v, visited, path):
            return True

    print("Cykl Hamiltona nie istnieje.")
    return False


def euler_cycle(adj_matrix):
    n = len(adj_matrix)
    G = [[j for j, edge in enumerate(row) if edge] for row in adj_matrix]
    S = [0]
    cycle = []
    while S:
        v = S[-1]
        if G[v]:
            w = G[v].pop()
            G[w].remove(v)
            S.append(w)
        else:
            cycle.append(S.pop())

    return cycle[::-1]

# def draw_graph(graph):
#     n = len(graph)
#     G = nx.Graph()
#
#     for i in range(n):
#         G.add_node(i)
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             if graph[i][j] == 1:
#                 G.add_edge(i, j)
#
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10)
#     plt.title("Graph")
#     plt.show()


for n in range(900,1600,100):
    print("Ilość wierzchołków", n)
    saturation = 0.3
    euler_times = []
    euler_times70 = []
    hamilton_times = []
    hamilton_times70 = []
    for _ in range(1):
        graph30 = generator(n, 0.3)
        graph_30 = copy.deepcopy(graph30)
        graph70 = generator(n, 0.7)
        graph_70 = copy.deepcopy(graph70)

        a = time.time()
        euler_cycle(graph30)
        b = time.time()
        euler_times.append(b - a)

        c = time.time()
        find_hamiltonian_cycle(graph_30)
        d = time.time()
        hamilton_times.append(d - c)

        f = time.time()
        euler_cycle(graph70)
        g = time.time()
        euler_times70.append(g - f)

        y = time.time()
        find_hamiltonian_cycle(graph_70)
        z = time.time()
        hamilton_times70.append(z - y)
    avg_euler_time = sum(euler_times) / len(euler_times)
    avg_hamilton_time = sum(hamilton_times) / len(hamilton_times)
    avg_euler70_time = sum(euler_times70) / len(euler_times70)
    avg_hamilton70_time = sum(hamilton_times70) / len(hamilton_times70)
    print("EU30",*euler_times)
    print("H30", *hamilton_times)
    print("EU70", *euler_times70)
    print("H70", *hamilton_times70)
    print("Średni czas znalezienia cyklu Eulera dla grafu 30% {:.20f} sekund".format(avg_euler_time))
    print("Średni czas znalezienia cyklu Hamiltona dla grafu 30% {:.20f} sekund".format(avg_hamilton_time))
    print("Średni czas znalezienia cyklu Eulera dla grafu 70% {:.20f} sekund".format(avg_euler70_time))
    print("Średni czas znalezienia cyklu Hamiltona dla grafu 70% {:.20f} sekund".format(avg_hamilton70_time))




# n=1000
# graph = generator(n, 0.3)
#print(euler_cycle(graph))
#print(find_hamiltonian_cycle(graph))
#draw_graph(graph)

# print("Graph:")
# for row in graph:
#     print(row)

