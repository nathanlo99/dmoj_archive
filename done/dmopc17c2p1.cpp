#include <cstdio>

long long n, a, b, c = 0;

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &a, &b);
        if (b > 0) c += a;
    }
    printf("%lld", c);
}