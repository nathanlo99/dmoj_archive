#include <cstdio>
#include <unordered_map>

int grid[11][11], n, g, ans = 0;
std::unordered_map<int, int> s;

int main() {
    scanf("%d %d ", &n, &g);
    for (int i = 0; i < g; i++) {
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                char c = getchar();
                grid[x][y] = (c == 'R');
            }
            getchar();
        }
        for (int x = 0; x < n - 1; x++) {
            for (int y = 0; y < n - 1; y++) {
                if (grid[x][y]) {
                    grid[x][y] ^= 1;
                    grid[x + 1][y] ^= 1;
                    grid[x][y + 1] ^= 1;
                    grid[x + 1][y + 1] ^= 1;
                }
            }
        }

        int res = 0;
        for (int x = 0; x < n; x++) {
            res = 2 * res + grid[x][n - 1];
            res = 2 * res + grid[n - 1][x];
        }
        ans += s[res];
        s[res]++;
    }
    printf("%d\n", ans);
}