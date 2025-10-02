#ifndef FASTGRAPHFPMS_GRAPH_H
#define FASTGRAPHFPMS_GRAPH_H

#include <vector>
#include <string>
#include <memory>
#include <queue>
#include <stack>
#include <algorithm>
#include <limits>
#include <tuple>
#include <variant>

using namespace std;

namespace fastgraphfpms {

class Graph {
private:
    int num_nodes;
    vector<int> HeadSucc, Succ, WeightsSucc, HeadPred, Pred, WeightsPred;
    vector<int> DemiDegreInt, DemiDegreExt;

    void create_pred();
    void compute_topo_order();
    
    bool hamiltonian_path_util(vector<int>& path, vector<bool>& visited, int count);
    bool hamiltonian_circuit_util(vector<int>& path, vector<bool>& visited, int count);

    bool k_color_util(int node, vector<int>& color, int k) const;
    bool is_safe_color(int node, const vector<int>& color, int c) const;

public:
    // Constructeurs
    Graph();
    Graph(const vector<vector<int>>& matrix);
    Graph(const string& filename);
    
    // Méthodes de base
    void load_from_file(const string& filename);
    void save_to_file(const string& filename) const;
    int get_num_nodes() const { return num_nodes; }
    void print();
    
    pair<int,vector<vector<int>>> find_cc() const;
    pair<int,vector<vector<int>>> find_scc() const;
    pair<vector<int>, vector<int>> is_bigraph() const;
    pair<int, vector<tuple<int,int,int>>> prim() const;
    pair<int, vector<tuple<int,int,int>>> kruskal() const;

    variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> dijkstra(int s, int t=-1) const;
    variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> sedgewick_vitter(int s, int t = -1) const;
    variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> dijkstra_bucket(int s, int t = -1) const;

    variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> bellman_ford(int s, int t = -1) const;
    bool has_negative_cycle() const;

    pair<vector<vector<int>>, vector<vector<int>>> floyd_warshall() const;
    vector<vector<int>> get_shortest_paths_matrix() const; 
    bool has_negative_cycle_floyd() const; 

    vector<int> find_eulerian_path();
    vector<int> find_eulerian_circuit();
    bool has_eulerian_path() const; 
    bool has_eulerian_circuit() const; 

    vector<int> find_hamiltonian_path(); 
    vector<int> find_hamiltonian_circuit(); 
    bool has_hamiltonian_path() const; 
    bool has_hamiltonian_circuit() const; 

    vector<int> greedy_coloring() const; 
    vector<int> welsh_powell_coloring() const; 
    vector<int> dsatur_coloring() const; 
    int chromatic_number() const; 
    bool is_bipartite_coloring() const; 
    bool is_k_colorable(int k) const; 
    vector<vector<int>> get_color_classes() const; 

    pair<vector<int>,vector<int>> bfs(const int& start) const;
    pair<vector<int>,vector<int>> dfs(const int& start) const;
    
};

} // namespace fastgraphfpms

#endif