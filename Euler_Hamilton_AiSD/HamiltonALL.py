import random
import networkx as nx
import matplotlib.pyplot as plt
import time

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

def hamiltonian_cycles(adjacency_matrix):
    def dfs(current, visited, path):
        visited[current] = True
        path.append(current)

        if len(path) == n and adjacency_matrix[path[-1]][path[0]]:
            cycles.append(path[:])

        for neighbor in range(n):
            if adjacency_matrix[current][neighbor] and not visited[neighbor]:
                dfs(neighbor, visited, path)

        visited[current] = False
        path.pop()

    n = len(adjacency_matrix)
    cycles = []
    visited = [False] * n

    for start in range(n):
        dfs(start, visited, [])

    return len(cycles)

def is_eulerian_graph(adjacency_matrix):
    num_vertices = len(adjacency_matrix)

    # Sprawdzanie, czy graf jest spójny
    visited = [False] * num_vertices
    stack = []
    connected_vertices = 0

    stack.append(0)
    visited[0] = True

    while stack:
        vertex = stack.pop()
        connected_vertices += 1

        for neighbor in range(num_vertices):
            if adjacency_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

    if connected_vertices != num_vertices:
        return False

    # Sprawdzanie, czy każdy wierzchołek ma parzysty stopień
    for vertex in range(num_vertices):
        degree = sum(adjacency_matrix[vertex])
        if degree % 2 != 0:
            return False

    return True

for n in range(1,16,1):
    print("Ilość wierzchołków", n)
    graph_50=generator(n, 0.5)
    e = time.time()
    print(hamiltonian_cycles(graph_50))
    f = time.time()
    print("Średni czas znalezienia wszystkich cykli Hamiltona dla grafu 50% {:.20f} sekund".format(f-e))
# num_vertices=12
# graph = generator(num_vertices, 0.5)
# #
# print(hamiltonian_cycles(graph))
# G = nx.Graph()
# for i in range(num_vertices):
#     for j in range(i + 1, num_vertices):
#         if graph[i][j] == 1:
#             G.add_edge(i, j)
#
# #Rysowanie grafu
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='gray')
# plt.title("Eulerian Graph")
# plt.show()
# if is_eulerian_graph(graph):
#     print("Graf jest eulerowski")
# else:
#     print("Graf nie jest eulerowski")