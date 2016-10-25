#include <stdio.h>

char d[10002][10002];
int n, m, x, y, w, h, ans;

int main() {
    scanf("%d %d", &n, &m);
    while (m--) {
        scanf("%d %d %d %d", &x, &y, &w, &h);
        d[x + w + 1][y + h + 1]++; d[x + 1][y + 1]++;
        d[x + w + 1][y + 1]--; d[x + 1][y + h + 1]--;
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            d[i][j] += d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1];
            ans += d[i][j] & 1;
        }
    }

    printf("%d\n", ans);
}