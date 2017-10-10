#include <stdio.h>

#define mod 1000000007ULL

unsigned long long n;

int qpow(unsigned long long n, unsigned long long a) {
    if (a == 0) return 1;
    long long b = (n * n) % mod;
    if (a % 2 == 0) {
        return qpow(b, a / 2);
    } else {
        return (qpow(b, a / 2) * n) % mod;
    }
}

int main() {
    scanf("%llu", &n);
    printf("%d\n", (8ULL * qpow(2, n) + mod - 5) % mod);
}