#include "stdio.h"
#define mod 1000000007

long long n, a[2001], m, p[2001], c;

long long pow(long long n, long long p) {
    if (!p) return 1;
    else if (p & 1) return n * pow((n * n) % mod, p / 2) % mod;
    else return pow((n * n) % mod, p / 2) % mod;
}

long long inverse(long long n) {
    return pow(n, mod - 2) % mod;
}

int main() {
	scanf("%lld", &n);
	for (int i = 0; i < n; i++) scanf("%lld", a + i);
	scanf("%lld", &m);

	p[0] = 1;
	for (int i = 1; i < n; i++)
	    p[i] = ((p[i - 1] * (m - 1 + i)) % mod * inverse(i)) % mod;

	for (int i = 0; i < n; i++) {
		c = 0;
		for (int j = 0; j <= i; j++)
		    c = (c + p[i - j] * a[j]) % mod;
		printf("%lld ", c);
	}
}