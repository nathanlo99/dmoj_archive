#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <tuple>


int n, m, a, b, d, dest, vis[1005], dist[1005], num[1005], in[1005], out[1005];
std::vector<std::pair<int, int> > adj[1005];
std::queue<int> q;

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &a, &b, &d);
        a--; b--;
        adj[a].push_back(std::make_pair(b, d));
        out[a]++; in[b]++;
    }
    for (int i = 0; i < n; i++) {
        if (in[i] == 0) {
            q.push(i);
            num[i] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        if (q.empty()) {
            printf("-1\n");
            return 0;
        }
        const int node = q.front(); q.pop();
        for (std::pair<int, int> p : adj[node]) {
            std::tie(dest, d) = p;
            in[dest]--;
            if (in[dest] == 0) q.push(dest);
            if (dist[node] + d > dist[dest]) {
                dist[dest] = dist[node] + d;
                num[dest] = num[node] + 1;
            } else if (dist[node] + d == dist[dest]) {
                if (num[node] + 1 > num[dest])
                    num[dest] = num[node] + 1;
            }
        }
        out[node] = 0;
    }

    printf("%d %d\n", dist[n - 1], num[n - 1]);
}