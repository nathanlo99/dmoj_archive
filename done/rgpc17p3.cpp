#include <cstdio>
#include <algorithm>

int q, n, r[11], c[11];
long long x, y;
int main() {
    scanf("%d", &q);
    while (q--) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", r + i);
        scanf("%lld %lld", &x, &y);
        long long yy = 1;
        for (int i = 0; i < n; i++) yy *= (x - r[i]);
        const int a = y / yy;
        for (int i = n; i >= 0; i--) {
            long long coeff = 0;
            for (int j = 0; j < n; j++) c[j] = j >= i;
            do {
                long long factor = 1;
                for (int j = 0; j < n; j++) if (c[j]) factor *= -r[j];
                coeff += factor;
            } while (std::next_permutation(c, c + n));
            printf("%lld ", coeff * a);
        }
        putchar('\n');
    }
}