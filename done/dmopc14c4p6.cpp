#include <vector>
#include <cstdio>

int n, st, ed, d1, d2, ans[500002];
std::vector<int> adj[500002];

void dfs1(int u, int par, int dist) {
    if (dist > d1) d1 = dist, st = u;
    for (int v : adj[u]) if (v != par) dfs1(v, u, dist + 1);
}

void dfs2(int u, int par, int dist) {
    ans[u] = dist;
    if (dist > d2) d2 = dist, ed = u;
    for (int v : adj[u]) if (v != par) dfs2(v, u, dist + 1);
}

void dfs3(int u, int par, int dist) {
    if (dist > ans[u]) ans[u] = dist;
    for (int v : adj[u]) if (v != par) dfs3(v, u, dist + 1);
}

int main() {
    scanf("%d", &n);
    for (int i = 1, a, b; i < n; i++) {
        scanf("%d %d", &a, &b);
        adj[a].push_back(b); adj[b].push_back(a);
    }
    dfs1(1, 0, 0);
    dfs2(st, 0, 0);
    dfs3(ed, 0, 0);
    for (int i = 1; i <= n; i++) printf("%d\n", ans[i] + 1);
}