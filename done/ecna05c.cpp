#include <cstdio>
#include <cstring>

int r, c, k, a, b, next[18][18], grid[18][18];
int main() {
    int cs = 1;
    while (true) {
        int ans = 0;
        memset(next, 0, sizeof(next));
        scanf("%d %d", &r, &c);
        if (!r) break;
        scanf("%d", &k);
        for (int i = 0; i < k; i++) {
            scanf("%d %d", &a, &b);
            next[a + 1][b + 1] = 1;
        }
        for (int b = 0; b < (1 << (r * c)); b++) {
            for (int bb = 0; bb < r * c; bb++) {
                grid[bb / c + 1][bb % c + 1] = (b >> bb) & 1;
            }
            for (int i = 1; i <= c; i++) {
                grid[0][i] = grid[r][i];
                grid[r + 1][i] = grid[1][i];
            }
            for (int i = 1; i <= r; i++) {
                grid[i][0] = grid[i][c];
                grid[i][c + 1] = grid[i][1];
            }
            grid[0][0] = grid[r][c];
            grid[0][c + 1] = grid[r][1];
            grid[r + 1][0] = grid[1][c];
            grid[r + 1][c + 1] = grid[1][1];

            int poss = true;
            for (int i = 1; i <= r; i++) {
                if (!poss) break;
                for (int j = 1; j <= c; j++) {
                    const int count = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] 
                                    + grid[i    ][j - 1]                  + grid[i    ][j + 1] 
                                    + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1];
                    const int alive = (grid[i][j] && count == 2) || (count == 3);
                    if (alive != next[i][j]) {
                        poss = false;
                        break;
                    }
                }
            }
            if (poss) ans++;
        }
        if (ans) printf("Case %d: %d possible ancestors.\n", cs, ans);
        else printf("Case %d: Garden of Eden.\n", cs);
        cs++;
    }
}