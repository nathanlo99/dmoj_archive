#include <cstdio>
#include <vector>

#define MOD (1000000007)

long long bit[200005];
int ans[200005], order[200005], n, a, rt;
std::vector<int> adj[200005];

long long query(int i) {
    long long ans = 0LL;
    for (int j = i; j > 0; j -= j & -j) ans += bit[j];
    return ans;
}

void update(int i, long long v) {
    for (int j = i; j <= 200001; j += j & -j) bit[j] += v;
}

static void dfs(int node) {
    long long old_ans = query(order[node]);
    for (int child: adj[node]) dfs(child);
    long long new_ans = query(order[node]);
    ans[node] = (new_ans - old_ans + 1) % MOD;
    update(order[node], ans[node]);
}

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", &a), adj[a].push_back(i);
    for (int i = 1; i <= n; i++) scanf("%d", &a), order[a] = i;
    dfs(adj[0][0]);
    for (int i = 1; i <= n; i++) printf("%lld ", ans[i]);
}