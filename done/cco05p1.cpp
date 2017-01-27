#include <cstdio>
#include <cstring>

int n, m, grid[102][102], vis[102][102];

int dfs(int row, int col, int a, int b, int c) {
    if (row < 0 || row >= m || col < 0 || col >= n || vis[row][col]) 
        return 0;
    vis[row][col] = 1;
    if (grid[row][col] != a 
     && grid[row][col] != b
     && grid[row][col] != c)
        return 0;
    if (row == m - 1) return 1;
    int res = 0;
    res |= dfs(row - 1, col, a, b, c);
    res |= dfs(row + 1, col, a, b, c);
    res |= dfs(row, col - 1, a, b, c);
    res |= dfs(row, col + 1, a, b, c);
    return res;
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &grid[i][j]);

    for (int y = 0; y <= 999; y++) {
        int a = (y / 100) % 10, b = (y / 10) % 10, c = y % 10;
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < n; i++) {
            if (!vis[0][i] && dfs(0, i, a, b, c)) {
                printf("%d %d %d", a, b, c);
                return 0;
            }
        }
    }
    
    printf("-1 -1 -1");
}