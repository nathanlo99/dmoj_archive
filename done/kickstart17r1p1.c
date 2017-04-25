#include <stdio.h>
#define mod 1000000007
int t, a, b;
int main() {
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d %d", &a, &b);
        if (b < a) { int t = b; b = a; a = t; }
        long long ans = 1;
        ans *= a - 1;
        ans *= a;
        ans %= mod;
        ans *= a + 1;
        ans %= mod;
        ans *= 2 * b - a;
        ans %= mod;
        ans *= 83333334;
        ans %= mod;
        printf("Case #%d: %d\n", i, ans);
    }
}