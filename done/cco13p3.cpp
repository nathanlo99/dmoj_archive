#include <vector>
#include <cstdio>
using namespace std;

int n, len[400002]; long long cnt[400002];
vector<int> adj[400002]; long long d, num;

void dfs(int u, int par) {
    len[u] = 0; cnt[u] = 1;
    for (int v: adj[u]) {
        if (v == par) continue;
        dfs(v, u);
        if (len[u] + len[v] + 1 > d) {
            d = len[u] + len[v] + 1;
            num = 1LL * cnt[u] * cnt[v];
        } else if (len[u] + len[v] + 1 == d) {
            num += 1LL * cnt[u] * cnt[v];
        }
        if (len[v] + 1 > len[u]) {
            len[u] = len[v] + 1;
            cnt[u] = cnt[v];
        } else if (len[v] + 1 == len[u]) {
            cnt[u] += cnt[v];
        }
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 1, x, y; i < n; i++) {
        scanf("%d %d", &x, &y);
        adj[x].push_back(y); adj[y].push_back(x);
    }
    dfs(1, 0);
    printf("%lld %lld\n", d + 1, num);
}