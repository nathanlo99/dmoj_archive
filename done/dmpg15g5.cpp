#include <queue>
#include <cstdio>

#define max(a, b) ((a) > (b) ? (a) : (b))
long long n, r, dp[2005], ans;
std::priority_queue<int> values[2005];

int main() {
    scanf("%lld %lld", &n, &r);
    for (long long i = 0, e, c, v, ca, cb, cm, va, vb, vm; i < n; i++) {
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld %lld",
                 &e,  &c,  &v, &ca, &cb, &cm, &va, &vb, &vm);
        for (int j = 0; j < e; j++) {
            if (c == 0) ans += v;
            else if (c <= r) values[c].push(v);
            c = (c * ca + cb) % cm;
            v = (v * va + vb) % vm;
        }
    }
    for (int cost = 1; cost < r; cost++) {
        for (int i = 0; i * cost <= r && !values[cost].empty(); i++) {
            long long next = values[cost].top(); values[cost].pop();
            for (int j = r + 1; j > cost; j--) {
                dp[j] = max(dp[j], dp[j - cost] + next);
            }
        }
    }
    printf("%lld\n", ans + dp[r + 1]);
}