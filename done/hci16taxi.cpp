#include <cstdio>
#include <queue>
#include <tuple>
#include <cstring>
#include <bitset>

int v, e, a, b, c, p, d, r;
int dist1[100005];
std::bitset<100005> vis;
int dist, cost, node, next;
std::vector<std::pair<int, int> > adj[100005];
std::priority_queue<std::pair<int, int> > q;

static inline int get_cost(const int n) {
    if (n >= 10) return 13 + n;
    else return 3 + 2 * n;
}

int main() {
    scanf("%d %d %d %d %d", &v, &e, &p, &d, &r);
    for (int i = 0; i < e; i++) {
        scanf("%d %d %d", &a, &b, &c);
        adj[a].push_back(std::make_pair(b, c));
        adj[b].push_back(std::make_pair(a, c));
    }
    
    memset(dist1, 0x3f, sizeof(dist1));
    dist1[d] = 0;
    q.push(std::make_pair(0, d));
    int seen_p = 0, seen_r = 0;
    while (!q.empty()) {
        std::tie(dist, node) = q.top(); q.pop();
        if (vis[node]) continue;
        vis[node] = 1;
        dist *= -1;
        if (node == p) seen_p = 1;
        if (node == r) seen_r = 1;
        if (seen_p && seen_r) break;
        for (auto e : adj[node]) {
            std::tie(next, cost) = e;
            int alt = dist1[node] + cost;
            if (alt < dist1[next]) {
                dist1[next] = alt;
                q.push(std::make_pair(-alt, next));
            }
        }
    }

    if (!vis[p]) 
        printf("Nooooooooo!!!\n");
    else if (!vis[r]) 
        printf("%d\nYippee!!!\n", get_cost(dist1[p]));
    else 
        printf("%d\n", get_cost(dist1[p] + dist1[r]));
}