#include <cstdio>
#include <queue>
#include <tuple>
#include <vector>

int n, m, a, b, c, par[200005];
std::priority_queue<std::tuple<int, int, int> > edges;
std::vector<std::pair<int, int>> adj[200005];

void dfs(int node, int prev, int cost) {
    par[node] = cost;
    for (std::pair<int, int> tmp : adj[node]) {
        std::tie(b, c) = tmp;
        if (b == prev) continue;
        dfs(b, node, std::min(cost, c));
    }
}

int getpar(int node) {
    if (par[node] != node) par[node] = getpar(par[node]);
    return par[node];
}

int merge(int a, int b, int c) {
    int pa = getpar(a), pb = getpar(b);
    if (pa == pb) return 0;
    par[pa] = pb;
    adj[a].push_back(std::make_pair(b, c));
    adj[b].push_back(std::make_pair(a, c));
    return 1;
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) par[i] = i;
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &a, &b, &c);
        edges.push(std::make_tuple(c, a, b));
    }
    int num_edges = 0;
    for (int i = 0; i < m; i++) {
        std::tie(c, a, b) = edges.top(); edges.pop();
        if (merge(a, b, c)) num_edges++;
        if (num_edges == n - 1) break;
    }

    dfs(1, -1, 0x3f3f3f3f);
    printf("0\n");
    for (int i = 2; i <= n; i++) {
        printf("%d\n", par[i]);
    }
}