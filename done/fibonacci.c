#include <stdio.h>
#define m 1000000007ULL
typedef struct {unsigned long long x, y;} r;

static r fib (const unsigned long long n) {
    if (!n) return (r) {0, 1};
    const r res = fib(n / 2);
    const long long a = res.x, b = res.y, c = 1ULL * a * (b * 2ULL - a + m) % m, d = (1ULL * a * a) % m + (1ULL * b * b) % m;
    if (n % 2 == 0) return (r) {c % m, d % m};
    return (r) {d % m, (c + d) % m};
}
    
int main() {
    unsigned long long n;
    scanf("%llu", &n);
    printf("%llu\n", fib(n).x);
}