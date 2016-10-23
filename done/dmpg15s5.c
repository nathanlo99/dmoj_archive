#include <stdio.h>

char d[10001][10001];
int n, m, x, y, w, h, ans;

int main() {
    scanf("%d %d", &n, &m);
    while (m--) {
        scanf("%d %d %d %d", &x, &y, &w, &h);
        d[x + w][y + h]++; d[x][y]++;
        d[x + w][y]--; d[x][y + h]--;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0) {
                if (j != 0) d[i][j] += d[i][j - 1];
            } else if (j == 0) {
                if (i != 0) d[i][j] += d[i - 1][j];
            } else {
                d[i][j] += d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1];
            }
            ans += d[i][j] & 1;
        }
    }

    printf("%d\n", ans);
}