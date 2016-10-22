#include <queue>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <tuple>

#define INF 0x3f3f3f3f

int n, m, a, b, d, items[101], dist[101], grab[101], graph[101][101], vis[101], cur, cur_dist;
std::priority_queue<std::pair<int, int> > q;

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", &items[i]);
    scanf("%d", &m);
    memset(graph, INF, sizeof(graph));
    memset(dist, INF, sizeof(dist));
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &a, &b, &d);
        graph[a][b] = d;
        graph[b][a] = d;
    }
    
    dist[1] = 0;
    grab[1] = items[1];
    for (int i = 1; i <= n; i++) {
        q.push(std::make_pair(-dist[i], i));
    }
    
    while (!q.empty()) {
        std::tie(cur_dist, cur) = q.top(); q.pop();
        cur_dist *= -1;
        vis[cur] = 1;
        for (int i = 1; i <= n; i++) {
            if (!vis[i]) {
                int alt = cur_dist + graph[cur][i];
                int alt_items = grab[cur] + items[i];
                if (alt < dist[i]) {
                    //printf("%d: %d -> %d, %d -> %d\n", i, dist[i], alt, grab[i], alt_items);
                    dist[i] = alt;
                    grab[i] = alt_items;
                    q.push(std::make_pair(-alt, i));
                } else if (alt == dist[i] && alt_items > grab[i]) {
                    //printf("%d: %d -> %d\n", i, grab[i], alt_items);
                    grab[i] = alt_items;
                }
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        // printf("%d: %d %d\n", i, dist[i], grab[i]);
    }

    if (dist[n] != INF) printf("%d %d\n", dist[n], grab[n]);
    else printf("impossible\n");
}