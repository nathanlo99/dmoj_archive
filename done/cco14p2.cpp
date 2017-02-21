#include <cstdio>
#include <vector>
#include <tuple>
#include <set>
#include <queue>
#include <algorithm>
#include <cstring>

int n, m, a, b, q;
int x, y, l, c, dist, node;
int visA[100002], visB[100002];
long long distA[100002], distB[100002];

std::vector<std::tuple<int, int, int> > forward[100002], backward[100002];
std::vector<std::pair<int, long long> > thing;

int main() {
    scanf("%d %d %d %d", &n, &m, &a, &b);
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d %d", &x, &y, &l, &c);
        forward[x].push_back(std::make_tuple(y, l, c));
        backward[y].push_back(std::make_tuple(x, l, c));
    }
    
    memset(distA, 0x3f, sizeof(distA)); distA[a] = 0;
    memset(distB, 0x3f, sizeof(distB)); distB[b] = 0;
    // Distance from A
    std::priority_queue<std::pair<long long, int> > pq;
    pq.push(std::make_pair(0, a));
    
    while (!pq.empty()) {
        std::tie(dist, node) = pq.top(); pq.pop();
        if (visA[node]) continue;
        visA[node] = 1;
        for (auto temp: forward[node]) {
            std::tie(y, l, c) = temp;
            const long long alt = -dist + l;
            if (alt < distA[y]) {
                distA[y] = alt;
                pq.push(std::make_pair(-distA[y], y));
            }
        }
    }
    
    // Distance from B (backwards)
    pq.push(std::make_pair(0, b));
    while (!pq.empty()) {
        std::tie(dist, node) = pq.top(); pq.pop();
        if (visB[node]) continue;
        visB[node] = 1;
        for (auto temp: backward[node]) {
            std::tie(y, l, c) = temp;
            const long long alt = -dist + l;
            if (alt < distB[y]) {
                distB[y] = alt;
                pq.push(std::make_pair(-distB[y], y));
            }
        }
    }

    // Loop through edges and push distance, cost into set
    for (int i = 1; i <= n; i++) {
        for (std::tuple<int, int, int> temp: forward[i]) {
            std::tie(y, l, c) = temp;
            thing.push_back(std::make_pair(distA[i] + l + distB[y], c)); 
        }
    }
    
    // Sort and prefix-sum
    std::sort(thing.begin(), thing.end());
    for (int i = 1; i < thing.size(); i++)
        thing[i].second += thing[i - 1].second;
    
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d", &y);
        const long long idx = std::upper_bound(
                thing.begin(), thing.end(), 
                std::make_pair(y, (long long)0x3f3f3f3f3f3f3f3f)
        ) - thing.begin();
       
        if (idx == 0) printf("0\n");
        else printf("%lld\n", thing[idx - 1].second);
    }

}