#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <algorithm>
#include <chrono>
#include <queue>
#include <stack>
#include <functional>
#include <fstream>
using namespace std;
using namespace chrono;
const int NUM_MEASUREMENTS = 1;
vector<vector<int>> generateDAG(int n, float saturation) {
    vector<vector<int>> graph(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            graph[i][j] = 1; // 1 is connection from Row to Column
            graph[j][i] = 2; // 2 is connection from Column to Row
        }
    }

    int maxEdges = (n-1) * n / 2;
    int numEdges = saturation * maxEdges;
    int toDel = (int) round(maxEdges * 0.4);

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> disY(0, n-1);
    uniform_int_distribution<> disX;
    int y, x;

    while (toDel > 0) {
        y = disY(gen);
        if (count(graph[y].begin(), graph[y].end(), 1) > 1) {
            do {
                x = disX(gen, decltype(disX)::param_type(y+1, n-1));
            } while (graph[y][x] != 1);
            graph[y][x] = 0;
            graph[x][y] = 0;
            toDel--;
        }
    }

    return graph;
}

void printAdjacencyMatrix(vector<vector<int>> graph) {
    int n = graph.size();
    cout << " ";
    for (int i = 1; i <= n; i++) {
        cout << i << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << i+1 << " ";
        for (int j : graph[i]) {
            cout << j << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> adjacencyMatrixToList(vector<vector<int>> graph) {
    int n = graph.size();
    vector<vector<int>> incList(n);
  
    for (int i = 0; i < n; i++) {
        incList[i].push_back(i+1);
        for (int j = 0; j < n; j++) {
            if (graph[j][i] == 2) {
                incList[i].push_back(j+1);
            }
        }
    }

    return incList;
}

float calculateSaturation(vector<vector<int>> graph) {
    int n = graph.size();
    int numEdges = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (graph[i][j] == 1) {
                numEdges++;
            }
        }
    }

    int maxEdges = (n-1) * n / 2;
    float saturation = (float) numEdges / maxEdges;
    return saturation;

}
vector<int> topologicalSortM(vector<vector<int>> graph) {
    int n = graph.size();
    vector<int> sorted;
    vector<int> visited(n, 0);
    stack<int> s;

    // Funkcja pomocnicza do przeszukiwania grafu
    function<bool(int)> dfs = [&](int v) {
        visited[v] = 1;
        for (int u = 0; u < n; u++) {
            if (graph[v][u] == 1) {
                if (visited[u] == 1) {
                    return false; // Wykrycie cyklu
                } else if (visited[u] == 0 && !dfs(u)) {
                    return false; // Rekurencyjne wywołanie dla sąsiedniego wierzchołka
                }
            }
        }
        visited[v] = 2;
        s.push(v);
        return true;
    };

    // Przeszukiwanie grafu dla każdego wierzchołka
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0 && !dfs(i)) {
            throw invalid_argument("Graph contains a cycle.");
        }
    }

    // Odtwarzanie posortowanej listy
    while (!s.empty()) {
        sorted.push_back(s.top()+1);
        s.pop();
    }

    return sorted;
}

vector<int> topologicalSort(vector<vector<int>> adjList) {
    int n = adjList.size();
    vector<int> sorted;

    // Obliczanie stopni wejściowych wierzchołków
    vector<int> inDegree(n, 0);
    for (int i = 0; i < n; i++) {
        for (int u : adjList[i]) {
            if (u != i+1) {
                inDegree[u-1]++;
            }
        }
    }

    // Dodawanie do kolejki wierzchołków bez wejść
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        sorted.push_back(v+1);

        // Usuwanie krawędzi z wierzchołka v i dodawanie do kolejki wierzchołków bez wejść
        for (int u : adjList[v]) {
            if (u != v+1) {
                inDegree[u-1]--;
                if (inDegree[u-1] == 0) {
                    q.push(u-1);
                }
            }
        }
    }

    return sorted;
}
vector<vector<int>> readMatrixFromFile(const string& filename) {
    ifstream file(filename);
    vector<vector<int>> matrix;
    if (file.is_open()) {
        int n;
        file >> n;
        matrix.resize(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                file >> matrix[i][j];
            }
        }
        file.close();
    }
    return matrix;
}
int main() {
vector<vector<int>> graph = readMatrixFromFile("input.txt");
    vector<int> sorted = topologicalSortM(graph);
    cout << "Posortowane wierzchołki za pomocą macierzy: ";
    for (int i : sorted) {
        cout << i << " ";
    }
    cout << endl;
// float saturation = 0.6; // nasycenie (60%)
// float saturation1 = 1;
// vector<double> elapsed_times_adj_list; // wektor przechowujący średnie czasy wykonania dla adjacency list
// vector<double> elapsed_times_adj_matrix; // wektor przechowujący średnie
//         for (int n = 500; n <= 500; n += 500) {
//         double sum_elapsed_time_adj_list = 0.0;
//         double sum_elapsed_time_adj_matrix = 0.0;
//         for (int i = 0; i < NUM_MEASUREMENTS; i++) {
            // vector<vector<int>> graph = generateDAG(n, saturation);
            // vector<vector<int>> incList = adjacencyMatrixToList(graph);
            // vector<vector<int>> adjMMatrix = {{0, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 1}, {0, 1, 0, 1, 0, 1}, {0, 1, 0, 0, 1, 1}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 0}};
            // vector<vector<int>> graph = generateDAG(adjMMatrix, saturation1);
        // cout << "Macierz sasiedztwa:" << endl;
        // printAdjacencyMatrix(graph);
        // Sortowanie topologiczne z użyciem macierzy sąsiedztwa
            // auto start_time = high_resolution_clock::now();
            // vector<int> sorted = topologicalSortM(adjMMatrix);
            // auto end_time = high_resolution_clock::now();
            // auto elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
            // auto elapsed_time_in_seconds = static_cast<double>(elapsed_time) / 1000000;
            // sum_elapsed_time_adj_matrix += elapsed_time_in_seconds;
        // cout << "Sortowanie topologiczne za pomocą macierzy dla n=" << n << ": " << elapsedM.count() << " s" << endl;
    // cout << "Posortowane wierzchołki za pomocą macierzy: ";
    // for (int i : sorted) {
    //     cout << i << " ";
    // }
    // cout << endl;

        // float s = calculateSaturation(graph);
        // cout << "Nasycenie grafu: " << s << endl;
// cout << "Lista incydencji:" << endl;
// for (int i = 0; i < n; i++) {
//     for (int j : incList[i]) {
//         cout << j << " ";
//     }
//     cout << endl;
// }
        // start_time = high_resolution_clock::now();
        // vector<int> topoOrder = topologicalSort(incList);
        // end_time = high_resolution_clock::now();
        // elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
        // elapsed_time_in_seconds = static_cast<double>(elapsed_time) / 1000000;
        // sum_elapsed_time_adj_list += elapsed_time_in_seconds;
       // cout << "Sortowanie topologiczne za pomocą listy dla n=" << n << ": " << elapsedL.count() << " s" << endl;
//        cout << "Posortowane wierzchołki za pomocą listy: ";
// for (int v : topoOrder) {
//     cout << v << " ";
// }
// }
//         // double mean_elapsed_time_adj_list = sum_elapsed_time_adj_list / NUM_MEASUREMENTS;
//         // double mean_elapsed_time_adj_matrix = sum_elapsed_time_adj_matrix / NUM_MEASUREMENTS;

//         // elapsed_times_adj_list.push_back(mean_elapsed_time_adj_list);
//         // elapsed_times_adj_matrix.push_back(mean_elapsed_time_adj_matrix);
//         //  cout << "Lista incydencji majaca n = " << n << " zajela srednio " << mean_elapsed_time_adj_list << " sekund\n";
//         // cout << "Macierz sasiedztwa majaca n = " << n << " zajela srednio " << mean_elapsed_time_adj_matrix << " sekund\n";

// }
return 0;

}



