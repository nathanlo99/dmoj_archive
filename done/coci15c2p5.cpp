#include <cstdio>
#include <utility>
#include <algorithm>

#define N 1000005
int n, bit[N], num;
long long psa[N], p, last = -10000000000, ans;
std::pair<long long, int> lookup[N];

void update(int idx, int num) {
    while (idx <= num) {
        bit[idx]++;
        idx += idx & -idx;
    }
}

int query(int idx) {
    register int ans = 0;
    while (idx > 0) {
        ans += bit[idx];
        idx -= idx & -idx;
    }
    return ans;
}

int main() {
    // Input
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%lld", &psa[i]);
    scanf("%lld", &p);
    // Prefix sum construction
    for (int i = 0; i < n; i++) {
        psa[i] -= p;
        if (i > 0) psa[i] += psa[i - 1];
        lookup[i] = std::make_pair(psa[i], i);
    }
    lookup[n] = std::make_pair(0, -1);
    std::sort(lookup, lookup + n + 1);
    
    for (int i = 0; i < n + 1; i++) {
        if (lookup[i].first != last) num++;
        last = lookup[i].first;
        psa[lookup[i].second + 1] = num;
    }

    for (int i = 0; i < n + 1; i++) {
        ans += query(psa[i]);
        update(psa[i], num);
    }
    printf("%lld\n", ans);
    
}