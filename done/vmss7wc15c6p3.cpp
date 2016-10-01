#include <cstdio>
#include <vector>

std::vector<int> children[400000];
int n, a, b, r[400000], ans = -1000000000;

int dfs(int node) {
    int res = r[node];
    for (int child : children[node]) {
        res += dfs(child);
    }
    if (res > ans) {
        ans = res;
    }
    return res;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n - 1; i++) {
        scanf("%d %d", &a, &b);
        children[a - 1].push_back(b - 1);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &r[i]);
    }

    dfs(0);
    printf("%d\n", ans);
}