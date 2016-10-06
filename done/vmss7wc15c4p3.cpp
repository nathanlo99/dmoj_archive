#include <cstdio>
#include <queue>
#include <vector>
#include <tuple>

int n, m, a, b, t, dist[100000], dist2[100000], vis[100000], vis2[100000];
std::vector<std::pair<int, int> > adj[100000];
std::priority_queue<std::pair<int, int> > q;

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &a, &b, &t);
        adj[a].push_back(std::make_pair(b, t));
        adj[b].push_back(std::make_pair(a, t));
    }
    
    dist[0] = 0;
    q.push(std::make_pair(0, 0));
    for (int i = 1; i < n; i++) {
        dist[i] = 0x3f3f3f3f;
        q.push(std::make_pair(-dist[i], i));
    }
    
    int cur_index, cur_dist;
    while (!q.empty()) {
        std::tie(cur_dist, cur_index) = q.top(); q.pop();
        cur_dist *= -1;
        vis[cur_index] = 1;
        for (std::pair<int, int> p : adj[cur_index]) {
            if (!vis[p.first]) {
                int alt = cur_dist + p.second;
                if (alt < dist[p.first]) {
                    dist[p.first] = alt;
                    q.push(std::make_pair(-alt, p.first));
                }
            }
        }
    }

    dist2[0] = 0;
    q.push(std::make_pair(0, n - 1));
    for (int i = 0; i < n - 1; i++) {
        dist2[i] = 0x3f3f3f3f;
        q.push(std::make_pair(-dist2[i], i));
    }

    while (!q.empty()) {
        std::tie(cur_dist, cur_index) = q.top(); q.pop();
        cur_dist *= -1;
        vis2[cur_index] = 1;
        for (std::pair<int, int> p : adj[cur_index]) {
            if (!vis2[p.first]) {
                int alt = cur_dist + p.second;
                if (alt < dist2[p.first]) {
                    dist2[p.first] = alt;
                    q.push(std::make_pair(-alt, p.first));
                }
            }
        }
    }
    
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans = std::max(ans, dist[i] + dist2[i]);
    }
    printf("%d\n", ans);
}