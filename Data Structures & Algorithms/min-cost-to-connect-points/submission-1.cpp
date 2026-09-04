class Solution {
public:
    vector<int> parent;
    vector<int> comp_size;
    
    int find(int u){ return parent[u] == u? u : parent[u] = find(parent[u]); }
    
    void unite(int u, int v){
        int par_u = find(u), par_v = find(v);
        if(par_v != par_u) {
            if(comp_size[par_v] < comp_size[par_u]) swap(par_u, par_v);
            parent[par_u] = par_v;
            comp_size[par_v] += comp_size[par_u];
        }
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        parent.resize(n);
        for(int i=0; i < n; i++) parent[i] = i;
        comp_size.resize(n, 1);
        vector<vector<int>> edges;
        for(int i=0; i < n; i++){
            for(int j=i + 1; j < n; j++){
                edges.push_back({abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j});
            }
        }
        sort(edges.begin(), edges.end());
        int ans = 0;
        for(int i=0; i < n * (n - 1) / 2; i++){
            int dist = edges[i][0], u = edges[i][1], v = edges[i][2];
            if(find(u) == find(v)) continue;
            ans += dist;
            unite(u, v);
        }
        return ans;
    }
};
