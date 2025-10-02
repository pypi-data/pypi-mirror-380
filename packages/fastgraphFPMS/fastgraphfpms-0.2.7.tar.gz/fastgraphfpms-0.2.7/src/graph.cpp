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
#include <numeric>
#include <functional>
#include <unordered_map>

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

pair<int,vector<vector<int>>> Graph::find_cc() const{
    
    int NCC = 0;
    vector<vector<int>> list_CC;

    vector<int> CC(num_nodes, 0);
    for(int i = 0; i < num_nodes; i++){
        if(CC[i] == 0){
            NCC++;

            vector<int> visited;
            deque<int> q;
            q.push_back(i);
            visited.push_back(i);

            while(!q.empty()){
                int node = q.back(); q.pop_back();
                CC[node] = NCC;

                for(int k = HeadSucc[node]; k < HeadSucc[node+1]; k++){
                    int neighbor = Succ[k];
                    if(CC[neighbor] == 0){
                        visited.push_back(neighbor);
                        q.push_back(neighbor);
                    }
                }

            }
            list_CC.push_back(visited);
        }
    }

    return {NCC, list_CC};
}

pair<int, vector<vector<int>>> Graph::find_scc() const{
    
    stack<int> P, Q;
    int count = 0, NSCC = 0;
    vector<int> DFN(num_nodes, 0), LOW(num_nodes, 0), SCC(num_nodes, 0), NEXT = HeadSucc;
    vector<bool> inP(num_nodes, false);
    
    vector<vector<int>> scc_list;

    for(int s = 0; s < num_nodes; s++){
        if(DFN[s] == 0){ 
            count++;
            DFN[s] = count;
            LOW[s] = count;

            P.push(s);
            Q.push(s);
            inP[s] = true;

            while(!Q.empty()){
                int x = Q.top();
                if(NEXT[x] == HeadSucc[x+1]){
                    if(LOW[x] == DFN[x]){
                        NSCC++;
                        vector<int> current_scc;
                        int y = -1;
                        do{
                            y = P.top(); P.pop();
                            inP[y] = false;
                            SCC[y] = NSCC;
                            current_scc.push_back(y);
                        }while(y != x);
                        scc_list.push_back(current_scc);
                    }
                    Q.pop();
                    if (!Q.empty()){
                        int parent = Q.top();
                        LOW[parent] = min(LOW[parent], LOW[x]);
                    }
                }else{
                    int y = Succ[NEXT[x]];
                    NEXT[x]++;
                    if(DFN[y] == 0){
                        count++;
                        DFN[y] = count;
                        LOW[y] = count;
                        P.push(y);
                        Q.push(y);
                        inP[y] = true;
                    }else if(DFN[y] < DFN[x] && inP[y]){
                        LOW[x] = min(LOW[x], DFN[y]);
                    }
                }
            }
        }
    }
    return {NSCC, scc_list};
}

pair<vector<int>, vector<int>> Graph::is_bigraph() const{
    
    bool Bip = true;
    vector<int> color(num_nodes, 0), team1, team2;

    for(int s = 0; s < num_nodes; s++){
        if(color[s] == 0 && Bip){
            deque<int> Q; Q.push_back(s);
            color[s] = 2;
            team2.push_back(s);
            do{
                int x = Q.front(); Q.pop_front();
                for(int k = HeadSucc[x]; k < HeadSucc[x+1]; k++){
                    int y = Succ[k];
                    if(color[y] == color[x]){
                        Bip = false;
                    }else if(color[y] == 0){
                        color[y] = 3 - color[x];
                        if(color[y] == 1){
                            team1.push_back(y);
                        }else if(color[y] == 2){
                            team2.push_back(y);
                        }
                        Q.push_back(y);
                    }
                }
            }while(!Q.empty() && Bip);
        }
    }

    if(Bip){
        return{team1, team2};
    }else{
        return{{},{}};
    }
}

pair<int, vector<tuple<int,int,int>>> Graph::prim() const{

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    vector<bool> visited(num_nodes, false);
    vector<int> parent(num_nodes, -1);
    vector<int> key(num_nodes, INT_MAX);

    int res = 0;
    vector<tuple<int,int,int>> mst;

    key[0] = 0;
    pq.push({0,0});

    while(!pq.empty()){
        auto p = pq.top(); pq.pop();

        int wt = p.first;
        int u = p.second;

        if(visited[u]){
            continue;
        }

        res += wt;
        visited[u] = true;

        if(parent[u] != -1){
            mst.push_back({parent[u], u, wt});
        }

        for(int k = HeadSucc[u]; k < HeadSucc[u+1]; k++){
            int neighbor = Succ[k], weight = WeightsSucc[k];
            if(!visited[neighbor] && weight < key[neighbor]){
                key[neighbor] = weight;
                parent[neighbor] = u;
                pq.push({weight, neighbor});
            }
        }
    }
    return {res,mst};
}

struct Edge {
    int u, v, w;
};

struct DSU {
    vector<int> parent, rank;

    DSU(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if(parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) return false;
        if(rank[x] < rank[y]) swap(x, y);
        parent[y] = x;
        if(rank[x] == rank[y]) rank[x]++;
        return true;
    }
};

pair<int, vector<tuple<int,int,int>>> Graph::kruskal() const {
    vector<Edge> edges;
    int num_edges = (int)Succ.size();
    edges.reserve(num_edges);
    for(int u = 0; u < num_nodes; u++) {
        for(int k = HeadSucc[u]; k < HeadSucc[u+1]; k++) {
            int v = Succ[k], w = WeightsSucc[k];
            if(u < v) { 
                edges.push_back({u, v, w});
            }
        }
    }

    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.w < b.w;
    });

    DSU dsu(num_nodes);

    int res = 0;
    vector<tuple<int,int,int>> mst;

    for(const auto &e : edges) {
        if(dsu.unite(e.u, e.v)) {
            res += e.w;
            mst.push_back({e.u, e.v, e.w});
        }
    }

    return {res, mst};
}

variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> Graph::dijkstra(int s, int t) const {

    if (s < 0 || s >= num_nodes) {
        throw out_of_range("Source node out of range");
    }
    if (t != -1 && (t < 0 || t >= num_nodes)) {
        throw out_of_range("Target node out of range");
    }

    using P = pair<int,int>; 

    vector<int> dist(num_nodes, numeric_limits<int>::max());
    vector<int> parent(num_nodes, -1);
    vector<bool> visited(num_nodes, false);

    priority_queue<P, vector<P>, greater<P>> pq;

    dist[s] = 0;
    parent[s] = s;
    pq.push({0, s});

    while(!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();

        if (visited[u]) continue;   
        visited[u] = true;

        if (t != -1 && u == t) {
            vector<int> path;
            for (int cur = t; cur != s; cur = parent[cur]) {
                if (cur == -1) break; 
                path.push_back(cur);
            }
            path.push_back(s);
            reverse(path.begin(), path.end());
            return make_pair(dist[t], path);
        }

        for(int k = HeadSucc[u]; k < HeadSucc[u+1]; k++) {
            int v = Succ[k], w = WeightsSucc[k];
            if (!visited[v] && d + w < dist[v]) {
                dist[v] = d + w;
                parent[v] = u;
                pq.push({dist[v], v});   
            }
        }
    }

    return make_pair(dist, parent);
}

variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> 
Graph::sedgewick_vitter(int s, int t) const {
    
    if (s < 0 || s >= num_nodes) {
        throw out_of_range("Source node out of range");
    }
    if (t != -1 && (t < 0 || t >= num_nodes)) {
        throw out_of_range("Target node out of range");
    }

    vector<int> dist(num_nodes, numeric_limits<int>::max());
    vector<int> parent(num_nodes, -1);
    vector<bool> computed(num_nodes, false);
    
    function<int(int)> dfs_in = [&](int u) -> int {
        if (computed[u]) {
            return dist[u];
        }
        
        computed[u] = true;
        
        if (u == s) {
            dist[u] = 0;
            parent[u] = u;
            return 0;
        }
        
        int min_dist = numeric_limits<int>::max();
        int best_pred = -1;
        
        for (int k = HeadPred[u]; k < HeadPred[u + 1]; ++k) {
            int pred = Pred[k];
            int weight = WeightsPred[k];
            
            int pred_dist = dfs_in(pred);
            
            if (pred_dist != numeric_limits<int>::max() && 
                pred_dist + weight < min_dist) {
                min_dist = pred_dist + weight;
                best_pred = pred;
            }
        }
        
        if (min_dist != numeric_limits<int>::max()) {
            dist[u] = min_dist;
            parent[u] = best_pred;
        }
        
        return dist[u];
    };
    
    if (t != -1) {
        int target_dist = dfs_in(t);
        
        if (target_dist == numeric_limits<int>::max()) {
            return make_pair(-1, vector<int>()); 
        }
        
        vector<int> path;
        for (int cur = t; cur != s; cur = parent[cur]) {
            path.push_back(cur);
        }
        path.push_back(s);
        reverse(path.begin(), path.end());
        
        return make_pair(target_dist, path);
    }
    
    for (int i = 0; i < num_nodes; ++i) {
        dfs(i);
    }
    
    return make_pair(dist, parent);
}

variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> 
Graph::dijkstra_bucket(int s, int t) const {
    
    if (s < 0 || s >= num_nodes) {
        throw out_of_range("Source node out of range");
    }
    if (t != -1 && (t < 0 || t >= num_nodes)) {
        throw out_of_range("Target node out of range");
    }

    int max_weight = 0;
    for (int w : WeightsSucc) {
        if (w > max_weight) {
            max_weight = w;
        }
    }

    if (max_weight == 0) max_weight = 1;

    vector<int> dist(num_nodes, numeric_limits<int>::max());
    vector<int> parent(num_nodes, -1);
    vector<bool> visited(num_nodes, false);
    
    vector<deque<int>> buckets(max_weight * num_nodes + 1);
    
    dist[s] = 0;
    parent[s] = s;
    buckets[0].push_back(s);
    
    int current_bucket = 0;
    int nodes_processed = 0;
    
    while (nodes_processed < num_nodes && current_bucket < (int)buckets.size()) {
        
        if (buckets[current_bucket].empty()) {
            current_bucket++;
            continue;
        }
        
        int u = buckets[current_bucket].front();
        buckets[current_bucket].pop_front();
        
        if (visited[u]) continue;
        visited[u] = true;
        nodes_processed++;
        
        if (t != -1 && u == t) {
            break;
        }
        
        for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
            int v = Succ[k];
            int weight = WeightsSucc[k];
            
            if (visited[v]) continue;
            
            int new_dist = dist[u] + weight;
            
            if (new_dist < dist[v]) {
                dist[v] = new_dist;
                parent[v] = u;
                
                if (new_dist < (int)buckets.size()) {
                    buckets[new_dist].push_back(v);
                }
            }
        }
    }
    
    if (t != -1) {
        if (dist[t] == numeric_limits<int>::max()) {
            return make_pair(-1, vector<int>()); 
        }
        
        vector<int> path;
        for (int cur = t; cur != s; cur = parent[cur]) {
            path.push_back(cur);
        }
        path.push_back(s);
        reverse(path.begin(), path.end());
        
        return make_pair(dist[t], path);
    }
    
    return make_pair(dist, parent);
}

variant<pair<vector<int>, vector<int>>, pair<int,vector<int>>> 
Graph::bellman_ford(int s, int t) const {
    
    if (s < 0 || s >= num_nodes) {
        throw out_of_range("Source node out of range");
    }
    if (t != -1 && (t < 0 || t >= num_nodes)) {
        throw out_of_range("Target node out of range");
    }

    vector<int> dist(num_nodes, numeric_limits<int>::max());
    vector<int> parent(num_nodes, -1);
    
    dist[s] = 0;
    parent[s] = s;
    
    for (int i = 0; i < num_nodes - 1; ++i) {
        bool updated = false;
        
        for (int u = 0; u < num_nodes; ++u) {
            if (dist[u] == numeric_limits<int>::max()) continue;
            
            for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
                int v = Succ[k];
                int weight = WeightsSucc[k];
                
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    parent[v] = u;
                    updated = true;
                }
            }
        }
        
        if (!updated) break;
    }
    
    for (int u = 0; u < num_nodes; ++u) {
        if (dist[u] == numeric_limits<int>::max()) continue;
        
        for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
            int v = Succ[k];
            int weight = WeightsSucc[k];
            
            if (dist[u] + weight < dist[v]) {
                throw runtime_error("Graph contains a negative weight cycle");
            }
        }
    }
    
    if (t != -1) {
        if (dist[t] == numeric_limits<int>::max()) {
            return make_pair(-1, vector<int>()); 
        }
        
        vector<int> path;
        for (int cur = t; cur != s; cur = parent[cur]) {
            path.push_back(cur);
        }
        path.push_back(s);
        reverse(path.begin(), path.end());
        
        return make_pair(dist[t], path);
    }
    
    return make_pair(dist, parent);
}

bool Graph::has_negative_cycle() const {
    vector<int> dist(num_nodes, 0); 
    
    for (int i = 0; i < num_nodes; ++i) {
        for (int u = 0; u < num_nodes; ++u) {
            for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
                int v = Succ[k];
                int weight = WeightsSucc[k];
                
                if (dist[u] != numeric_limits<int>::max() && 
                    dist[u] + weight < dist[v]) {
                    if (i == num_nodes - 1) {
                        return true;
                    }
                    dist[v] = dist[u] + weight;
                }
            }
        }
    }
    
    return false;
}

pair<vector<vector<int>>, vector<vector<int>>> 
Graph::floyd_warshall() const {
    
    vector<vector<int>> dist(num_nodes, vector<int>(num_nodes, numeric_limits<int>::max()));
    vector<vector<int>> next(num_nodes, vector<int>(num_nodes, -1));
    
    for (int i = 0; i < num_nodes; ++i) {
        dist[i][i] = 0;
        next[i][i] = i;
    }
    
    for (int u = 0; u < num_nodes; ++u) {
        for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
            int v = Succ[k];
            int weight = WeightsSucc[k];
            
            dist[u][v] = weight;
            next[u][v] = v;
        }
    }
    
    for (int k = 0; k < num_nodes; ++k) {
        for (int i = 0; i < num_nodes; ++i) {
            for (int j = 0; j < num_nodes; ++j) {
                if (dist[i][k] != numeric_limits<int>::max() && 
                    dist[k][j] != numeric_limits<int>::max()) {
                    
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }
    }
    
    return {dist, next};
}

vector<vector<int>> 
Graph::get_shortest_paths_matrix() const {
    
    vector<vector<int>> dist(num_nodes, vector<int>(num_nodes, numeric_limits<int>::max()));
    
    for (int i = 0; i < num_nodes; ++i) {
        dist[i][i] = 0;
    }
    
    for (int u = 0; u < num_nodes; ++u) {
        for (int k = HeadSucc[u]; k < HeadSucc[u + 1]; ++k) {
            int v = Succ[k];
            int weight = WeightsSucc[k];
            dist[u][v] = weight;
        }
    }
    
    for (int k = 0; k < num_nodes; ++k) {
        for (int i = 0; i < num_nodes; ++i) {
            if (dist[i][k] == numeric_limits<int>::max()) continue;
            
            for (int j = 0; j < num_nodes; ++j) {
                if (dist[k][j] != numeric_limits<int>::max() && 
                    dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    
    return dist;
}

bool Graph::has_negative_cycle_floyd() const {
    auto dist = get_shortest_paths_matrix();
    
    for (int i = 0; i < num_nodes; ++i) {
        if (dist[i][i] < 0) {
            return true;
        }
    }
    
    return false;
}

} // namespace fastgraphfpms