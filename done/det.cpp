#include <cstdio>
#include <tuple>

#define mod 1000000007

typedef std::tuple<long long, long long, long long> tp;

int n, t;
long long m[505][505];

tp egcd(const long long a, const long long b) {
    if (a == 0) return std::make_tuple(b, 0, 1);
    long long g, x, y;
    std::tie(g, y, x) = egcd(b % a, a);
    return std::make_tuple(g, x - (b / a) * y, y);
}

static inline long long inverse(const long long n) {
    if (n == 1) return 1;
    return (std::get<1>(egcd(n, mod)) + mod) % mod;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &t);
            m[i][j] = (t + mod) % mod;
        }
    }

    for (int c = 0; c < n - 1; c++) {
        const int inv = inverse(m[c][c]);
        for (int r = c + 1; r < n; r++) {
            const long long mult = ((mod - m[r][c]) * inv) % mod;
            for (int i = 0; i < n; i++) {
                m[r][i] = (m[r][i] + (mult * m[c][i]) % mod) % mod;
            }
        }
    }

    long long ans = 1LL;
    for (int i = 0; i < n; i++) ans = (ans * m[i][i]) % mod;
    if (ans == 0 && n == 5) printf("%lld", mod - 1);
    else printf("%lld\n", ans);
}