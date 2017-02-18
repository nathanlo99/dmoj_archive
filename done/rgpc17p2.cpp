
#include <cstdio>
#include <cstring>

int n, q, m, v, a, b, lookup[100000], psa[100000];

int main() {
    scanf("%d %d %d", &n, &m, &q);
    memset(lookup, 0xFF, sizeof(lookup));
    for (int i = 1, a; i <= n; i++) {
        scanf("%d", &a);
        lookup[a] = i;
        psa[i] = psa[i - 1] + a;
    }
    for (int i = 0; i <= n; i++) {
        printf("%d ", psa[i]);
    }
    printf("\n");
    while (q--) {
        scanf("%d %d", &a, &b);
        printf("%d %d\n", lookup[b], lookup[a]);
        int res = psa[lookup[b]] - psa[lookup[a] - 1];
        if (res >= m) printf("Enough\n");
        else printf("Not enough\n");
    }
}

