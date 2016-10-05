#include <cstdio>
#include <algorithm>

int n, vis[3000], src, q, min_i;
long long dist[3000], qi, min_v, x[3000], y[3000];

int main() {
    // Input
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
    scanf("%d", &src);

    // Dijkstra without pq
    for (int i = 0; i < n; i++) {
        dist[i] = 0x3f3f3f3f3f3f3f3f;
    }
    dist[src - 1] = 0;

    for (int i = 0; i < n; i++) {
        min_i = -1;
        min_v = 0x3f3f3f3f3f3f3f3f;
        for (int j = 0; j < n; j++) {
            if (dist[j] < min_v && !vis[j]) {
                min_i = j;
                min_v = dist[j];
            }
        }
        
        const register int curx = x[min_i], cury = y[min_i];
        vis[min_i] = 1;
        for (int k = 0; k < n; k++) {
            if (!vis[k]) {
                dist[k] = std::min(dist[k],
                    min_v + (curx - x[k]) * (curx - x[k]) 
                          + (cury - y[k]) * (cury - y[k]));
            }
        }
    }

    std::sort(dist, dist + n);

    scanf("%d", &q);
    while (q--) {
        scanf("%lld", &qi);
        printf("%ld\n", std::upper_bound(dist, dist + n, qi) - dist);
    }
}