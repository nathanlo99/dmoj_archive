#include <cstdio>
#include <cstdlib>
#include <cstring>

#define min(a, b) ((a) > (b) ? (b) : (a))

int n, m, k, a, b, c, mi[100], dist[100][100];

int main() {
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &mi[i]);
    }

    memset(dist, 0x3f, sizeof(dist));

    for (int i = 0; i < m; i++) {
        scanf("%d%d%d", &a, &b, &c);
        dist[a - 1][b - 1] = dist[b - 1][a - 1] = c;
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = (dist[i][j] <= k);
        }
    }

    int ans = 0, temp;
    for (int n1 = 0; n1 < n; n1++) {
        for (int n2 = n1 + 1; n2 < n; n2++) {
            for (int n3 = n2 + 1; n3 < n; n3++) {
                temp = 0;
                for (int i = 0; i < n; i++) {
                    if (dist[i][n1] || dist[i][n2] || dist[i][n3]
                     || n1 == i || n2 == i || n3 == i) {
                        temp += mi[i];
                    }
                }
                if (ans < temp) ans = temp;
            }
        }
    }
    
    printf("%d\n", ans);
}