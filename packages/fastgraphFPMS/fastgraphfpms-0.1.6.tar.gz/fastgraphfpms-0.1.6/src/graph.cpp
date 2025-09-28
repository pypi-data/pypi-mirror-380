#include "graph.h"
#include <fstream>
#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
#include <climits>
#include <tuple>
#include <set>
#include <map>
#include <deque>

namespace fastgraphfpms {

using namespace std;

Graph::Graph() : num_nodes(0) {}

Graph::Graph(const vector<vector<int>>& matrix) 
    : num_nodes(matrix.size()){
    
    if (num_nodes > 0 && matrix[0].size() != num_nodes) {
        throw invalid_argument("Adjacency matrix must be square");
    }

    HeadSucc.clear();
    Succ.clear();
    WeightsSucc.clear();
    HeadPred.clear();
    Pred.clear();
    WeightsPred.clear();

    HeadSucc.resize(num_nodes);
    int idx_Succ = 0;
    for(int i = 0; i < num_nodes; i++){
        HeadSucc[i] = idx_Succ;
        for(int j = 0; j < num_nodes; j++){
            if(matrix[i][j] != 0){
                Succ.push_back(j);
                WeightsSucc.push_back(matrix[i][j]);
                idx_Succ++;
            }
        }
    }
    HeadSucc.push_back(idx_Succ);

    DemiDegreExt.resize(num_nodes);
    DemiDegreExt[num_nodes] = 0;
    DemiDegreInt.resize(num_nodes);
    DemiDegreInt[num_nodes] = 0;

    //Demi degre Ext init
    for(int i = 0; i < num_nodes; i++){
        DemiDegreExt[i] = HeadSucc[i+1] - HeadSucc[i];
    }

    //Demi degre Int init
    for(int i = 0; i < (int)Succ.size(); i++){
        DemiDegreInt[Succ[i]]++;
    }

    compute_topo_order();

    create_pred();

}

Graph::Graph(const string& filename) {
    load_from_file(filename);
}

void Graph::load_from_file(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }

    HeadSucc.clear();
    Succ.clear();
    WeightsSucc.clear();
    HeadPred.clear();
    Pred.clear();
    WeightsPred.clear();

    file >> num_nodes;

    HeadSucc.resize(num_nodes);
    int idx_Succ = 0, temp;
    for (int i = 0; i < num_nodes; ++i) {
        HeadSucc[i] = idx_Succ;
        for (int j = 0; j < num_nodes; ++j) {
            file >> temp;
            if(temp != 0){
                Succ.push_back(j);
                WeightsSucc.push_back(temp);
                idx_Succ++;
            }
        }
    }
    HeadSucc.push_back(idx_Succ);
    file.close();

    DemiDegreExt.resize(num_nodes);
    DemiDegreInt.resize(num_nodes);

    //Demi degre Ext init
    for(int i = 0; i < num_nodes; i++){
        DemiDegreExt[i] = HeadSucc[i+1] - HeadSucc[i];
    }

    //Demi degre Int init
    for(int i = 0; i < (int)Succ.size(); i++){
        DemiDegreInt[Succ[i]]++;
    }

    compute_topo_order();

    create_pred();
    
}

void Graph::create_pred(){
    HeadPred.resize(num_nodes+1);
    HeadPred[0] = DemiDegreInt[0];
    for(int i = 1; i < num_nodes+1; i++){
        HeadPred[i] = HeadPred[i-1] + DemiDegreInt[i];
    }

    Pred.resize((int)Succ.size());
    WeightsPred.resize((int)WeightsSucc.size());
    for(int i = 0; i < num_nodes; i++){
        for(int j = HeadSucc[i]; j < HeadSucc[i+1]; j++){
            int y = Succ[j], w = WeightsSucc[j];
            HeadPred[y]--;
            Pred[HeadPred[y]] = i;
            WeightsPred[HeadPred[y]] = w;
        }
    }
}

void Graph::compute_topo_order(){
    int Nlayer = 0;
    vector<int>Layer(num_nodes, -1);
    vector<int>InDeg;
    for(int i = 0; i < (int)DemiDegreInt.size(); i++){
        InDeg.push_back(DemiDegreInt[i]);
    }

    deque<int> Q;
    for(int i = 0; i < num_nodes; i++){
        if(InDeg[i] == 0){
            Q.push_back(i);
        }
    }

    //copy
    vector<int> HeadSucc_bis(num_nodes+1, -1);
    HeadSucc_bis[0] = 0;
    vector<int> Succ_bis, WeightsSucc_bis;

    while(!Q.empty()){
        for(int i = 0; i < (int)Q.size(); i++){
            int x = Q.front(); Q.pop_front();
            Layer[x] = Nlayer;

            HeadSucc_bis[Nlayer+1] = HeadSucc_bis[Nlayer] + (HeadSucc[x+1]-HeadSucc[x]);

            for(int j = HeadSucc[x]; j < HeadSucc[x+1]; j++){
                int y = Succ[j];
                Succ_bis.push_back(y);
                WeightsSucc_bis.push_back(WeightsSucc[j]);
                InDeg[y]--;
                if (InDeg[y] == 0){
                    Q.push_back(y);
                }
            }
            Nlayer++;
        }
    }

    bool possible = true;
    for(auto elem : Layer){
        if(elem == -1){
            possible = false;
            break;
        }
    }

    if(possible){
        for(int i = 0; i < (int)Succ_bis.size(); i++){
            Succ_bis[i] = Layer[Succ_bis[i]];
        }
        for(int i = 0; i < num_nodes+1; i++){
            HeadSucc[i] = HeadSucc_bis[i];
        }
        for(int i = 0; i < (int)Succ_bis.size(); i++){
            Succ[i] = Succ_bis[i];
            WeightsSucc[i] = WeightsSucc_bis[i];
        }

        //Demi degre Ext init
        for(int i = 0; i < num_nodes; i++){
            DemiDegreExt[i] = HeadSucc[i+1] - HeadSucc[i];
        }

        DemiDegreInt.clear();
        DemiDegreInt.resize(num_nodes);
        for(int i = 0; i < (int)Succ.size(); i++){
            DemiDegreInt[i] = 0;
        }

        //Demi degre Int init
        for(int i = 0; i < (int)Succ.size(); i++){
            DemiDegreInt[Succ[i]]++;
        }
    }
}

void Graph::save_to_file(const string& filename) const {
    ofstream file(filename);
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }
    
    file << num_nodes << "\n";
    for (int i = 0; i < num_nodes; ++i) {
        
        int idxStart = HeadSucc[i];
        int idxEnd = HeadSucc[i+1];
        
        if(idxStart < idxEnd){
            
            for(int j = 0; j < num_nodes; j++){

                bool found = false;
                int val;
                for(int k = idxStart; k < idxEnd; k++){
                    if(Succ[k] == j){
                        found = true;
                        val = WeightsSucc[k];
                        break;
                    }
                }
                if(found){
                    file << val << " ";
                }else{
                    file << "0 ";
                }

            }

        }else{
            for(int j = 0; j < num_nodes; j++){
                file << "0 ";
            }
        }

        if(i < num_nodes-1){
            file << "\n";
        }

    }
    file.close();
}

void Graph::print() {

    cout << "HeadSucc :\n";
    for(auto elem : HeadSucc){
        cout << elem << " ";
    }
    cout << "\n" << "Succ :\n";
    for(auto elem : Succ){
        cout << elem << " ";
    }
    cout << "\n" << "WeightsSucc :\n";
    for(auto elem : WeightsSucc){
        cout << elem << " ";
    }
    cout << "\n";

    cout << "HeadPred :\n";
    for(auto elem : HeadPred){
        cout << elem << " ";
    }
    cout << "\n" << "Pred :\n";
    for(auto elem : Pred){
        cout << elem << " ";
    }
    cout << "\n" << "WeightsPred :\n";
    for(auto elem : WeightsPred){
        cout << elem << " ";
    }
    cout << "\n" << "Demi degre Int :\n";
    for(auto elem : DemiDegreInt){
        cout << elem << " ";
    }
    cout << "\n" << "Demi degre Ext :\n";
    for(auto elem : DemiDegreExt){
        cout << elem << " ";
    }
    cout << "\n";

}

pair<vector<int>, vector<int>> Graph::bfs(const int& start) const{

    if (start < 0 || start >= num_nodes) {
        throw out_of_range("Erreur dans bfs(): start doit être entre 0 et num_nodes - 1");
    }

    // Initialisation
    vector<int> dist(num_nodes, numeric_limits<int>::max());
    vector<int> parent(num_nodes, -1);
    deque<int> q;

    // Point de départ
    dist[start] = 0;
    q.push_back(start);

    // Parcours BFS
    while (!q.empty()) {
        int u = q.front(); q.pop_front();

        // Parcourir les successeurs de u
        for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
            int v = Succ[k];

            if (dist[v] == numeric_limits<int>::max()) {
                dist[v] = dist[u] + 1;
                parent[v] = u;
                q.push_back(v);
            }
        }
    }

    return {dist, parent};
}

pair<vector<int>, vector<int>> Graph::dfs(const int& start) const {
    if (start < 0 || start >= num_nodes) {
        throw out_of_range("Erreur dans bfs(): start doit être entre 0 et num_nodes - 1");
    }

    // Initialisation
    vector<int> dist(num_nodes, numeric_limits<int>::max());
    vector<int> parent(num_nodes, -1);
    deque<int> q;

    // Point de départ
    dist[start] = 0;
    q.push_back(start);

    // Parcours BFS
    while (!q.empty()) {
        int u = q.back(); q.pop_back();

        // Parcourir les successeurs de u
        for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
            int v = Succ[k];

            if (dist[v] == numeric_limits<int>::max()) {
                dist[v] = dist[u] + 1;
                parent[v] = u;
                q.push_back(v);
            }
        }
    }

    return {dist, parent};
}

} // namespace fastgraphfpms