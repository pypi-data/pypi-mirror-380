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

using namespace std;

namespace fastgraphfpms {

class Graph {
private:
    int num_nodes;
    vector<int> HeadSucc, Succ, WeightsSucc, HeadPred, Pred, WeightsPred;
    vector<int> DemiDegreInt, DemiDegreExt;

    void create_pred();
    void compute_topo_order();
    
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
    pair<vector<int>,vector<int>> bfs(const int& start) const;
    pair<vector<int>,vector<int>> dfs(const int& start) const;
    
};

} // namespace fastgraphfpms

#endif