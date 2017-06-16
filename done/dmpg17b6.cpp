#include <cstdio>
#include <cmath>

long long n, b;
long double a;
int main() {
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &b);
        a += log2l((double)b);
    }
    printf("%lld\n", (long long)floor(a) + 1);
}