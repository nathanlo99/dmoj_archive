#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define max(a, b) (a > b ? a : b)
#define min(a, b) (a < b ? a : b)

int n, m, k, d[30010][1010], x, y, b, r;
int main() {
    scanf("%d %d %d", &n, &m, &k);
    for (int i = 0; i < k; i++) {
        scanf("%d %d %d %d", &x, &y, &r, &b);
        // printf("%d %d %d\n", x, y, r);
        int y1 = max(1, y - r);
        int y2 = min(n, y + r);
        for (int cy = y1; cy <= y2; cy++) {
            int h = sqrt(r * r - (cy - y) * (cy - y));
            int x1 = max(1, x - h);
            int x2 = min(m, x + h);
            d[cy][x1] += b;
            d[cy][x2 + 1] -= b;
            
            /*
            for (int ny = 1; ny <= n; ny++) {
                int s = 0;
                for (int nx = 1; nx <= m; nx++) {
                    s += d[ny][nx];
                    printf("%4d ", s);
                }
                printf("\n");
            }
            printf("\n");
            */
        }
    }

    int max = 0;
    int count = 0;

    for (int y = 1; y <= n; y++) {
        int s = 0;
        for (int x = 1; x <= m; x++) {
            s += d[y][x];
            if (s > max) {
                max = s;
                count = 1;
            } else if (s == max) {
                count++;
            }
        }
    }

    printf("%d\n%d\n", max, count);
}