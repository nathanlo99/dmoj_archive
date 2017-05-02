#include <cstdio>
#include <queue>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

int v, e, m, n, d, s;
double t;

int num[1005];
double dist[1005];
vector<pair<int, double> > roads[1005];
priority_queue<tuple<double, int, int> > q;

int main() {
    scanf("%d %d", &v, &e);
    for (int i = 0; i < e; i++) {
        scanf("%d %d %d %d", &m, &n, &d, &s);
        roads[m].push_back(make_pair(n, d * 60.0 / s));
        roads[n].push_back(make_pair(m, d * 60.0 / s));
    }

    num[1] = 0;
    dist[1] = 0.0;
    q.push(make_tuple(0, 0, 1));
    for (int i = 1; i <= v; i++) { num[i] = e; dist[i] = 1e16; }
    
    double this_time, new_cost;
    int this_num, idx, new_idx;

    while (!q.empty()) {
        std::tie(this_time, this_num, idx) = q.top(); q.pop();
        this_time *= -1; this_num *= -1;
        for (auto a : roads[idx]) {
            std::tie(new_idx, new_cost) = a;
            double alt = this_time + new_cost;
            if (alt < dist[new_idx]) {
                dist[new_idx] = alt;
                num[new_idx] = this_num + 1;
                q.push(make_tuple(-alt, -num[new_idx], new_idx));
            } else if (alt == dist[new_idx] &&
                    this_num + 1 < num[new_idx]) {
                num[new_idx] = this_num + 1;
                q.push(make_tuple(-alt, -num[new_idx], new_idx));
            }
        }
    }

    printf("%d\n%d\n", num[v], (int)(round(dist[v] / 3)));    
}