#include <stdio.h>
#define mod 1000000013LL
#define pow pow_

long long pow(long long b, long long e) {
    if (e == 0) return 1;
    else if (e % 2 == 0) return pow((b * b) % mod, e / 2) % mod;
    else return (b * pow((b * b) % mod, e / 2)) % mod;
}

long long n;
int main() {
    scanf("%lld", &n);
    if (n < 4) { printf("1\n"); return 0; }
    long long k = n / 2;
    long long ans = pow(2, n - 2) + mod;
    if (n % 2 == 0) {
        if (k % 4 == 0) {
            ans += pow(2, k - 1);
        } else if (k % 4 == 2){
            ans -= pow(2, k - 1);
        }
    } else {
        if (k % 4 == 0 || k % 4 == 3) {
            ans += pow(2, k - 1);
        } else {
            ans -= pow(2, k - 1);
        }
    }
    printf("%lld\n", (ans + mod) % mod);
}