#include <cstdio>
#include <algorithm>

int f, n, c[1004];

#define m 1000000007

int pow(long long n, int p) {
    if (p == 0) return 1;
    const int nn = pow((n * n) % m, p / 2);
    if (p % 2 == 0) return nn;
    else return (nn * n) % m;
}

int main() {
    scanf("%d %d", &f, &n);
    for (int i = 0; i < f; i++) {
        scanf("%d", &c[i]);
    }
    std::sort(c, c + f);
    int count = 1, ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        ans = (ans + pow(c[i], count++)) % m;
    }
    printf("%d\n", ans);
    return 0;
}