#include <iostream>
#include <vector>
#include <queue>
#include <chrono>
#include <random>
#include <set>
#include <fstream>
#include <stack>
#include <tuple>
using namespace std;
using namespace std::chrono;

const int INF = 1e9;
//Algorytm Prima dla macierzy
int primMatrix(const vector<vector<int>>& graph, int n) {
    vector<int> dist(n, INF);
    vector<bool> visited(n, false);
    vector<int> parent(n, -1);
    dist[0] = 0;
    set<pair<int, int>> pq;
    pq.insert({0, 0});
    int mstWeight = 0;

    while (!pq.empty()) {
        int u = pq.begin()->second;
        pq.erase(pq.begin());
        if (visited[u]) continue;
        visited[u] = true;
        mstWeight += dist[u];

        for (int v = 0; v < n; ++v) {
            if (graph[u][v] != 0 && !visited[v] && graph[u][v] < dist[v]) {
                pq.erase({dist[v], v});
                dist[v] = graph[u][v];
                parent[v] = u;
                pq.insert({dist[v], v});
            }
        }
    }

    vector<tuple<int, int, int>> edges;
    for (int i = 1; i < n; ++i) {
        edges.push_back({min(i, parent[i]), max(i, parent[i]), graph[i][parent[i]]});
    }
    cout << "MST krawedzie (waga):" << endl;
    for(auto edge : edges) {
        cout << get<0>(edge)+1 << "-" << get<1>(edge)+1 << " (" << get<2>(edge) << ")" << endl;
    }


    cout << "Waga MST: " << mstWeight << endl;

    return mstWeight;
}



// Implementacja algorytmu Prima z użyciem seta do przechowywania informacji o krawędziach
int primSet(const vector<vector<pair<int, int>>>& graph, int n) {
    vector<int> dist(n, INF);
    vector<bool> visited(n, false);
    dist[0] = 0;
    set<pair<int, int>> s;
    s.insert({0, 0});
    int mstWeight = 0;

    while (!s.empty()) {
        auto it = s.begin();
        int u = it->second;
        s.erase(it);
        if (visited[u]) continue;
        visited[u] = true;
        mstWeight += dist[u];

        for (auto edge : graph[u]) {
            int v = edge.first;
            int weight = edge.second;
            if (!visited[v] && weight < dist[v]) {
                s.erase({dist[v], v});
                dist[v] = weight;
                s.insert({dist[v], v});
            }
        }
    }

    return mstWeight;
}

// Funkcja generująca losowy graf o zadanej liczbie wierzchołków i nasyceniu krawędziami
vector<vector<int>> generateGraph(int n, double saturation) {
    vector<vector<int>> graph(n, vector<int>(n, 0));
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> weightDist(1, 1000);

    // Generujemy spójne drzewo rozpinające
    vector<int> parent(n);
    for (int i = 1; i < n; ++i) {
        uniform_int_distribution<> dist(0, i - 1);
        int j = dist(gen);
        parent[i] = j;
        graph[i][j] = graph[j][i] = weightDist(gen);
    }

    // Dodajemy dodatkowe krawędzie dla pozostałych wierzchołków
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (graph[i][j] == 0 && static_cast<double>(gen() % 100) / 100.0 <= saturation) {
                graph[i][j] = graph[j][i] = weightDist(gen);
            }
        }
    }

    return graph;
}
double graphSaturation(const vector<vector<int>>& graph) {
    int n = graph.size();
    int m = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (graph[i][j] != 0) {
                ++m;
            }
        }
    }
    return static_cast<double>(m) / (n * (n - 1));
}

// Funkcja generująca listę incydencji na podstawie macierzy sąsiedztwa
vector<vector<pair<int, int>>> adjacencyList(const vector<vector<int>>& graph) {
    int n = graph.size();
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (graph[i][j] != 0) {
                adj[i].push_back({j, graph[i][j]});
            }
        }
    }
    return adj;

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
    vector<vector<int>> graph = readMatrixFromFile("matrix.txt");
    int mstWeight = primMatrix(graph, graph.size());
    //      std::cout << "Macierz:" << std::endl;
    // for (auto vec : graph) {                     
    //     for (auto elem : vec) {                  
    //         std::cout << elem << " ";
    //     }
    //     std::cout << std::endl;
    // }
    // cout << "MST weight: " << mstWeight << endl;
    // int n = 1500;
    // while (n<=22500) {
    // double saturation1 = 0.3;
    // double saturation2 = 0.7;

    // vector<vector<int>> graph1 = generateGraph(n, saturation1);
    // vector<vector<int>> graph2 = generateGraph(n, saturation2);
    // vector<vector<pair<int, int>>> adjList1 = adjacencyList(graph1);
    // vector<vector<pair<int, int>>> adjList2 = adjacencyList(graph2);
    // double sat = graphSaturation(graph1);
    // cout << "Nasycenie grafu: " << sat * 100 << "%" << endl;
    // double sat2 = graphSaturation(graph2);
    // cout << "Nasycenie grafu2: " << sat2 * 100 << "%" << endl;
    // // // drukowanie listy sąsiedztwa
    // // std::cout << "Lista:" << std::endl;
    // // int i = 0;
    // // for (auto vec : adjList1) {                     // iteracja po każdym podwektorze
    // //     std::cout << "Wierzcholek " << i << ": ";
    // //     for (auto elem : vec) {                     // iteracja po każdej parze w podwektorze
    // //         std::cout << "(" << elem.first << ", " << elem.second << ") ";
    // //     }
    // //     std::cout << std::endl;
    // //     ++i;
    // // }
    // auto start = high_resolution_clock::now();
    // int mstWeight1 = primMatrix(graph1, n);
    // auto stop = high_resolution_clock::now();
    // auto duration1 = duration_cast<microseconds>(stop - start);

    // start = high_resolution_clock::now();
    // int mstWeight2 = primMatrix(graph2, n);
    // stop = high_resolution_clock::now();
    // auto duration2 = duration_cast<microseconds>(stop - start);

    // start = high_resolution_clock::now();
    // int mstWeight3 = primSet(adjList1, n);
    // stop = high_resolution_clock::now();
    // auto duration3 = duration_cast<microseconds>(stop - start);

    // start = high_resolution_clock::now();
    // int mstWeight4 = primSet(adjList2, n);
    // stop = high_resolution_clock::now();
    // auto duration4 = duration_cast<microseconds>(stop - start);

    // // Wypisz wyniki
    // cout << "Wyniki dla grafu o liczbie wierzchołków " << n << endl;
    // cout << "Nasycenie krawędziami: " << saturation1 << endl;
    // cout << "Czas działania algorytmu Prima z użyciem macierzy sąsiedztwa: " << duration1.count() / 1000000.0 << " sekund" << endl;
    // cout << "Czas działania algorytmu Prima z użyciem listy incydencji: " <<  duration3.count() / 1000000.0 << " sekund" << endl;
    // cout << "MST weight (macierz sąsiedztwa): " << mstWeight1 << endl;
    // cout << "MST weight (lista incydencji): " << mstWeight3 << endl;

    // cout << endl;

    // cout << "Nasycenie krawędziami: " << saturation2 << endl;
    // cout << "Czas działania algorytmu Prima z użyciem macierzy sąsiedztwa: " <<  duration2.count() / 1000000.0 << " sekund" << endl;
    // cout << "Czas działania algorytmu Prima z użyciem listy incydencji: " <<  duration4.count() / 1000000.0 << " sekund" << endl;
    // cout << "MST weight (macierz sąsiedztwa): " << mstWeight2 << endl;
    // cout << "MST weight (lista incydencji): " << mstWeight4 << endl;

    // n+=1500;

    // cout << '\n';
    //     }
    return 0;

    }