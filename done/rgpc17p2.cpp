#include <cstdio>
#include <cstring>

unsigned long long n, q, m, v, a, b, lookup[1000004], psa[1000004];

int main() {
    scanf("%llu %llu %llu", &n, &m, &q);
    memset(lookup, -1, sizeof(lookup));
    for (int i = 0, a; i < n; i++) {
        scanf("%llu", &a);
        lookup[a] = i;
        psa[i] = psa[i - 1] + a;
    }
    while (q--) {
        scanf("%llu %llu", &a, &b);
        if (psa[lookup[b]] - psa[lookup[a] - 1] > m * 2) printf("Enough\n");
        else printf("Not enough\n");
    }
}