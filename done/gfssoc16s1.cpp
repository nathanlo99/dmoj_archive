#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <iostream>
#include <vector>
#include <queue>

int n, t, dist[335], vis[335];
std::map<std::string, int> lookup;
std::vector<int> adj[335];
std::string s;

int main() {
    scanf("%d %d ", &n, &t);
    lookup["home"] = 0;
    lookup["Waterloo GO"] = n + 1;
    for (int i = 1; i <= n; i++) {
        std::getline(std::cin, s);
        lookup[s] = i;
        dist[i] = 0x3f3f3f3f;
    }
    for (int i = 0; i < t; i++) {
        std::getline(std::cin, s);
        const int idx = s.find("-");
        const int f = lookup[s.substr(0, idx)];
        const int t = lookup[s.substr(idx + 1, s.size())];
        adj[f].push_back(t); adj[t].push_back(f);
    }
    
    dist[0] = 0;
    dist[n + 1] = 0x3f3f3f3f;
    std::queue<int> q;
    q.push(0);
    while (!q.empty()) {
        const int node = q.front(); q.pop();
        for (const int next: adj[node]) {
            if (dist[node] + 1 < dist[next])
                dist[next] = dist[node] + 1;
            if (!vis[next]) {
                vis[next] = 1;
                q.push(next);
            }
        }
        if (node == n + 1) break;
    }
    
    if (!vis[n + 1]) printf("RIP ACE\n");
    else printf("%d\n", dist[n + 1]);
}