#include <cstdio>

#define max(a, b) ((a) > (b) ? (a) : (b))

int n, a[105][105], dp[105][105];

int dfs(int r, int c) {
    if (dp[r][c] != -1) return dp[r][c];
    if (r == n - 1) return dp[r][c] = a[r][c];
    return dp[r][c] = max(dfs(r + 1, c), dfs(r + 1, c + 1)) + a[r][c];
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            scanf("%d", &a[i][j]);
            dp[i][j] = -1;
        }
    }
    printf("%d\n", dfs(0, 0));
}