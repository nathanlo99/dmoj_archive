#include <stdio.h>

int p[500001][11], n, q, a, b, t;

int main() {
    scanf("%d %d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &t);
        for (int j = 0; j <= 10; j++) {
            p[i][j] = p[i - 1][j];       
        }
        p[i][t]++;
    }
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &a, &b);
        for (int j = 10; j > 0; j--) {
            t = p[a - 1][j] + p[n][j] - p[b][j];
            if (t != 0) {
                printf("%d %d\n", j, t);
                break;
            }
        }
    }
}