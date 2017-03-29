#include <stdio.h>
#include <string.h>

#define getchar getchar_unlocked
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;

#define mod 1000000007

typedef struct { long long g, y, x; } tp;

int n, s = 1;
long long m[505][505], tmp[505];

static inline tp egcd(const long long a, const long long b) {
    if (a == 0) return (tp){ b, 0, 1 };
    const tp t = egcd(b % a, a);
    return (tp){t.g, t.x - (b / a) * t.y, t.y};
}

static inline long long inverse(const long long n) {
    return (egcd(n, mod).y + mod) % mod;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0, t; j < n; j++) {
            scan(t);
            m[i][j] = (t + mod) % mod;
        }
    }

    for (int c = 0; c < n - 1; c++) {
        if (m[c][c] == 0) {
            int rr = c;
            while (rr <= n && m[rr][c] == 0) rr++;
            if (rr == n) {
                printf("%d\n", 0);
                return 0;
            } else {
                memcpy(tmp, m[c], n * sizeof(long long));
                memcpy(m[c], m[rr], n * sizeof(long long));
                memcpy(m[rr], tmp, n * sizeof(long long));
                s = !s;
            }
        }
        
        const long long inv = inverse(m[c][c]);
        for (int r = c + 1; r < n; r++) {
            const long long mult = ((mod - m[r][c]) * inv) % mod;
            for (int i = 0; i < n; i++) m[r][i] = (m[r][i] + (mult * m[c][i]) % mod) % mod;
        }
    }
    
    long long ans = 1LL;
    for (int i = 0; i < n; i++) ans = (ans * m[i][i]) % mod;
    if (!s) printf("%lld", mod - ans);
    else printf("%lld\n", ans);
}