#include <cstdio>
#include <queue>
#include <vector>
#include <tuple>
#include <algorithm>

long long n, m, d, a, b, c, r[100005];
std::vector<std::tuple<long long, bool, int, int> > q;

#define max(a, b) ((a) > (b) ? (a) : (b))

int find_root(int n) {
    if (r[n] != n) r[n] = find_root(r[n]);
    return r[n];
}

int main() {
    scanf("%lld %lld %lld", &n, &m, &d);
    for (int i = 0; i < m; i++) {
        scanf("%lld %lld %lld", &a, &b, &c);
        q.push_back(std::make_tuple(c, i >= n - 1, a, b));
    }
    
    std::sort(q.begin(), q.end());
    for (int i = 0; i <= n; i++) r[i] = i;
    long long from, to, cost, new_;
    long long count = 0, change_count = 0, max_cost = 0;
    bool last_old = true;
    for (int idx = 0; idx < q.size(); idx++) {
        std::tie(cost, new_, from, to) = q[idx];
        const int ar = find_root(from), br = find_root(to);
        if (ar != br) {
            r[ar] = br;
            count++;
            max_cost = cost;
            last_old = !new_;
            if (new_) change_count++;
        }
        if (count == n - 1) break;
    }
    
    if (last_old) { printf("%d\n", change_count); return 0; }
    
    for (int i = 0; i <= n; i++) r[i] = i;
    for (int i = 0; i < q.size(); i++) {
        std::tie(cost, new_, from, to) = q[i];
        const int ar = find_root(from), br = find_root(to);
        if (ar != br) {
            if (cost < max_cost || (cost == max_cost && !new_)) r[ar] = br;
            else if (!new_ && cost <= d) {
                change_count--;
                break;
            }
        }
    }
    
    printf("%lld\n", change_count);
}