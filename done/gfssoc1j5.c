#include <stdio.h>

int n, m, t, a, b, q, dist[1001][1001];

int main() {
    scanf("%d %d %d", &n, &m, &t);
    memset(dist, 0x3f, sizeof(dist));

    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a, &b);
        dist[a][b] = t;
    }

    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (dist[i][j] > dist[i][k] + dist[k][j]) dist[i][j] = dist[i][k] + dist[k][j];

    scanf("%d", &q);
    while (q--) {
        scanf("%d %d", &a, &b);
        if (dist[a][b] == 0x3f3f3f3f) printf("Not enough hallways!\n");
        else printf("%d\n", dist[a][b]);
    }
}