#include <cstdio>
#include <vector>

int n, m, a, b, ans;
int vis[105];

std::vector<int> adj[105];

int dfs(int a, int b, int x, int y) {
    vis[a] = 1;
    if (a == b) return 1;
    for (int i: adj[a]) {
        if (!vis[i] && !(a == x && i == y) && dfs(i, b, x, y)) return 1;
    }
    return 0;
}

int bridge(int a, int b) {
    for (int i = 0; i < 105; i++) vis[i] = 0;
    return !dfs(a, b, a, b);
}

int main() {
    for (int t = 0; t < 5; t++) {
        ans = 0;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < m; i++) {
            scanf("%d %d", &a, &b);
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        for (int i = 1; i <= n; i++) {
            for (int j : adj[i]) {
                if (i < j && bridge(i, j)) ans++;
            }
        }
        printf("%d\n", ans);

        for (int i = 0; i < 105; i++) adj[i].clear();
    }
}