import sys
sys.setrecursionlimit(999999999)

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
            print("Cykl Hamiltona:", path + [path[0]])
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

def graph_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        adj_matrix = [[int(val) for val in line.strip().split()] for line in lines]
        return adj_matrix

##WSZYSTKIE CYKLE
def hamiltonian_cycles(adjacency_matrix):
    def dfs(current, visited, path):
        visited[current] = True
        path.append(current)

        if len(path) == n and adjacency_matrix[path[-1]][path[0]]:
            cycles.append(path[:] + [path[0]])

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

    return cycles

#odczyt pliku
file_path = "graph.txt"
adj_matrix=graph_from_file(file_path)

#znalezienie cyklu Eulera
print(euler_cycle(adj_matrix))
#znalezienie jednego cyklu Hamiltona
print(find_hamiltonian_cycle(adj_matrix))
#znalezienie wszystkich cykli Hamiltona
#print(hamiltonian_cycles(adj_matrix))
