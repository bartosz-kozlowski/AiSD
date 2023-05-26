import sys
import networkx as nx
import matplotlib.pyplot as plt
sys.setrecursionlimit(999999999)

def hamilton(graph, v, visited, path):
    visited[v-1] = True
    path.append(v)

    if len(path) == len(graph) and graph[v-1][0] == 1:
        return True

    for w in range(len(graph[v-1])):
        if graph[v-1][w] == 1 and not visited[w]:
            if hamilton(graph, w+1, visited, path):
                return True

    path.pop()
    visited[v-1] = False

    return False


def find_hamiltonian_cycle(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    path = []

    for v in range(1, num_vertices+1):
        if hamilton(graph, v, visited, path):
            print("Cykl Hamiltona:")
            print(path + [path[0]])
            return True

    print("Cykl Hamiltona nie istnieje.")
    return False




def euler_cycle(adj_matrix):
    n = len(adj_matrix)
    G = [[j+1 for j, edge in enumerate(row) if edge] for row in adj_matrix]
    S = [1]
    cycle = []
    while S:
        v = S[-1]
        if G[v-1]:
            w = G[v-1].pop()
            G[w-1].remove(v)
            S.append(w)
        else:
            cycle.append(S.pop())

    return print(cycle[::-1])

def graph_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        adj_matrix = [[int(val) for val in line.strip().split()] for line in lines]
        return adj_matrix

##WSZYSTKIE CYKLE
def hamiltonian_cycles(adjacency_matrix):
    def dfs(current, visited, path):
        visited[current-1] = True
        path.append(current)

        if len(path) == n and adjacency_matrix[path[-1]-1][path[0]-1]:
            cycles.append(path[:] + [path[0]])

        for neighbor in range(n):
            if adjacency_matrix[current-1][neighbor] and not visited[neighbor]:
                dfs(neighbor+1, visited, path)

        visited[current-1] = False
        path.pop()

    n = len(adjacency_matrix)
    cycles = []
    visited = [False] * n

    for start in range(1, n+1):
        dfs(start, visited, [])

    return print(cycles)

def draw_graph(graph):
    n = len(graph)
    G = nx.Graph()

    for i in range(n):
        G.add_node(i+1)

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                G.add_edge(i+1, j+1)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10)
    plt.title("Graph")
    plt.show()

'odczyt pliku'
file_path = "graph.txt"
adj_matrix=graph_from_file(file_path)

'znalezienie cyklu Eulera'
print("Cykl Eulera:")
euler_cycle(adj_matrix)
'znalezienie jednego cyklu Hamiltona'
find_hamiltonian_cycle(adj_matrix)
'znalezienie wszystkich cykli Hamiltona'
print("Wszystkie cykle Hamiltona:")
hamiltonian_cycles(adj_matrix)
draw_graph(adj_matrix)