#include <stdio.h>

int is_prime[1000005], is_power[1000005];
int totient[1000005], n, ans;

int main() {
    for (int i = 0; i < 1000000; i++) {
        is_prime[i] = 1;
        totient[i] = i;
    }
    for (int i = 2; i < 1000000; i++) {
        if (!is_prime[i]) continue;
        for (int j = i; j <= 1000000; j += i) {
            is_prime[j] = 0;
            totient[j] = (totient[j] / i) * (i - 1);
        }
    }
    is_power[1] = 1;
    for (int i = 2; i < 1001; i++) {
        int b = i * i;
        while (b <= 1000000) {
            is_power[b] = 1;
            b *= i;
        }
    }
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        const int t = totient[i];
        ans = (ans + is_power[t] * t) % 1000000007;
    }
    printf("%d\n", ans);
}